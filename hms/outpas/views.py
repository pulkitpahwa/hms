import datetime
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.forms.models import modelformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import Context,Template, RequestContext
from django.template.loader import get_template
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView
from django.core.mail import EmailMessage

from guardian.mixins import LoginRequiredMixin

from .models import Outpass
from .forms import OutpassCreateForm
from profiles.models import Student, HostelStaff, StaffUser
from attendance.models import Attendance, Holidays
from msg.models import HostelStaffMsg, StaffMsg, SuccessMsg

# must check elements in the templates, if enrollment_id.sex = F, display the column of permission received from the warden column in the status of outpass. And other features

min_out_time = datetime.time(15,00,00)
max_in_time  = datetime.time(10,00,00)


def check_date(start_date, start_time, end_date, end_time):
    ''' this function returns whether the permission is required or not.
    if the out_time is less than 3:00 pm. The time 3:00 pm is set by me, can be changed on request or suggestion by college administration.

    This method checks whether the leave period lies in holidays, if not then set permission_required = True. then message should be sent to the concerned faculty and staff.'''
    min_out_time = datetime.time(15,00,00)
    max_in_time  = datetime.time(10,00,00)

    holiday = Holidays.objects.all()
    list_holidays = []
    for day in holiday :
        list_holidays.append(day.date_of_holiday.strftime("%Y-%m-%d"))

    d = start_date
    if start_time > datetime.time(15,00,00):    
        if end_date != start_date:
            d = start_date + datetime.timedelta(1)
    elif end_time < datetime.time(10,00,00):
        if start_date != end_date :
            end_date = end_date + datetime.timedelta(-1)

    delta = datetime.timedelta(days = 1)
    dates = []
    while d <= end_date:
        dates.append(d.strftime("%Y-%m-%d"))
        d +=delta
    
    for day in dates:
        if day not in list_holidays:
            return True
        
    else : 
        return False


def girl_permission(user):
    if user.sex == "F":
        return True
    else:
        return False


def create_time(field):
    '''This method creates time from the strings'''
    return datetime.time(int(field[0:2]) , int(field[3:5]), int(field[6:8]))
        
def create_date(field):
    '''This method creates date from the strings'''
    year = field[0:field.find("-")]
    return datetime.date(int(field[0:4]) , int(field[5:7]), int(field[8:10])) 
    
def save_outpass(enrollment_id, start_date,start_time, end_date, end_time, going_to, reason,  girl_permission_required, staff_permission_required, outpass_state, outpass_save_mode ):
    
    outpass = Outpass.objects.create(enrollment_id = enrollment_id,from_date = start_date, from_time = start_time, return_date = end_date, return_time = end_time, going_to = going_to, reason = reason, girl_permission_required = girl_permission_required, staff_permission_required = staff_permission_required, outpass_state = outpass_state, outpass_save_mode = outpass_save_mode, outpass_generated=datetime.datetime.now())
    outpass.save()
    return outpass
    
    
def check_outpass_state(girl_permission_required, staff_permission_required):
    if staff_permission_required or girl_permission_required:
        outpass_state = "W"
    else:
        outpass_state = "P"
    return outpass_state    

def return_message(outpass):
    message = " Name : "+ str(outpass.enrollment_id) + "\n From date : " + str(outpass.from_date) + "\n From time : " + str(outpass.from_time) + "\n Return date : " + str(outpass.return_date)+ "\n Reason " + str(outpass.reason) + "\n Going to : " + str(outpass.going_to)
    return message
    
 
@login_required
def all_outpass(request):
#set permissions so that only hostelstaff can check this out
    a = get_template("outpas/all.html")
    outpass = Outpass.objects.all().order_by('-outpass_id')
    c = Context({'outpasses':outpass})
    html = a.render(c)
    return HttpResponse(html)	



@login_required
def my_all_outpass(request):
#set permissions so that only student can check this out
    a = get_template("outpas/my_all.html")
    student = Student.objects.get(enrollment_id = request.oser)
    my_outpass = Outpass.objects.filter(enrollment_id = student)
    c = Context({'outpasses':my_outpass})
    html = a.render(c)
    return HttpResponse(html)	


class CreateOutpass(LoginRequiredMixin, CreateView):
    model = Outpass
    form_class = OutpassCreateForm


    def post(self, request, *args, **kwargs):
    
        form = self.form_class(request.POST)
        going_to = request.POST['going_to']
        reason = request.POST['reason']
        outpass_save_mode = request.POST['outpass_save_mode']            
        start_time = create_time(request.POST['from_time'])
        end_time = create_time(request.POST['return_time'])
        start_date = create_date(request.POST['from_date'])
        end_date = create_date(request.POST['return_date'])
        enrollment_id = Student.objects.get(enrollment_id = self.request.user)
        outpass_generated = datetime.datetime.now()
        staff_permission_required = check_date(start_date,start_time, end_date, end_time) 
        girl_permission_required = girl_permission(enrollment_id)
        
        outpass_state = check_outpass_state(girl_permission_required, staff_permission_required)
        
        if form.is_valid():
            outpass_object = save_outpass(enrollment_id, start_date,start_time, end_date, end_time, going_to, reason, girl_permission_required, staff_permission_required, outpass_state, outpass_save_mode )
            
            outpass = Outpass.objects.get(outpass_id = outpass_object.outpass_id)
            
            if outpass.outpass_state == "W":
                message = return_message(outpass)
                if girl_permission_required :
                    hostel_staff = HostelStaff.objects.get(position = "Girls hostel warden")
                    hostel_staff_message = HostelStaffMsg.objects.create(message = message, hostel_staff = hostel_staff, student = enrollment_id, outpass = outpass_object)
                    hostel_staff_message.save()
                    return HttpResponseRedirect("/profiles")
                elif staff_permission_required :
                    staff = StaffUser.objects.get(name  = "Vikas Thada")
                    staff_message = StaffMsg.objects.create(message = message, staff = staff, student = enrollment_id, outpass = outpass_object )
                    staff_message.save()
                    return HttpResponseRedirect("/profiles")
#                email = EmailMessage('Hello',message, to = ['pulkitpahwa11@gmail.com'])
#                email = EmailMessage('Hello',message, to = ['pulkitpahwa11@gmail.com'])
#                email.send()
            #success_url = "/outpass/success"
            else :
                # send pdf of the outpass with the image in it
                success_url = "/apple"
            return HttpResponseRedirect('/outpass/success/')
        else:
            return HttpResponseRedirect('/outpass/failure/')

# another method to do this, but dont know how to perform the email function,and where to call it
#    def form_valid(self, form):
#        form.instance.enrollment_id = Student.objects.get(enrollment_id = self.request.user)
#        form.instance.outpass_generated = datetime.datetime.now()
#        form.instance.staff_permission_required = check_date(form.instance.from_date,form.instance.from_time, form.instance.return_date, form.instance.return_time) 
#        form.instance.girl_permission_required = girl_permission(Student.objects.get(enrollment_id = self.request.user))
#        if form.instance.staff_permission_required or form.instance.girl_permission_required:
#            form.instance.outpass_state = "W"
#        else:
#            form.instance.outpass_state = "P"
#        # either send the message here or in the class, just before the success_url. try both ways
#        return super(CreateOutpass, self).form_valid(form)

 
def success(request):
    a = get_template("outpas/permission_not_req.html") 
    c = Context({})
    html = a.render(c)
    return HttpResponse(html)	
 

def failure(request):
    a = get_template("outpas/permission_req.html") 
    c = Context({})
    html = a.render(c)
    return HttpResponse(html)	
 
#def check(request):
#   outpass = Outpass.objects.filter(enrollment_id = Student.objects.get(enrollment_id = request.user)).order_by(-"outpass_generated_at")[0]
#   if outpass.outpass_state = W: send message, sorry your outpass cant be processed
#   else : send SMS and pdf .


@login_required
def update_outpass(request):
    a = get_template("index.html")
    enrollment_id = request.GET['username']
    c = Context({'user':enrollment_id})
    html = a.render(c)
    return HttpResponse(html)	

