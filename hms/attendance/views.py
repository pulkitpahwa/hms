import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context,Template
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import DetailView, RedirectView, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required

from braces.views import SetHeadlineMixin

from .models import Attendance, Holidays
from .forms import HolidaysCreateForm, HolidaysUpdateForm, AttendanceUpdateForm
from profiles.models import Student, StaffUser, HostelStaff


# must check elements in the templates, if enrollment_id.sex = F, display the column of permission received from the warden column in the status of outpass. And other features

min_out_time = datetime.time(15,00,00)
max_in_time  = datetime.time(10,00,00)

#make sure to call this function if any change is made to the holidays object. In short call this inside the update holidays class and create holidays class


def check_date(start_date, start_time, end_date, end_time):
    ''' this function returns whether the permission is required or not.
    if the out_time is less than 3:00 pm. The time 3:00 pm is set by me, can be changed on request or suggestion by college administration.

    This method checks whether the leave period lies in holidays, if not then set permission_required = True. then message should be sent to the concerned faculty and staff.'''

    if start_time > min_out_time:    
        if end_date != start_date:
            d = start_date + datetime.timedelta(1)
    if end_time < max_in_time:
        if start_date != end_date :
            end_date = end_date + datetime.timedelta(-1)
    delta = datetime.timedelta(days = 1)
    dates = []
    while d <= end_date:
        dates.append(d.strftime("%Y-%m-%d"))
        d +=delta
    
    for day in dates:
        if day not in list_holiday:
            return True
        
    else : 
        return False

########################### request.user returns the username i.e. enrollment number of the student

@login_required
def my_attendance(request):
    try:
        a = get_template("attendance/index.html")
        user = User.objects.get(username = request.user)
        student = Student.objects.get(enrollment_id = user)
        attend = Attendance.objects.filter(enrollment_id = student)
        c = Context({'attend':attend})
    except:
    # design the except phase differently for hostel staff
        a = get_template("login.html")
        c = Context({})
    html = a.render(c)
    return HttpResponse(html)	


#the permission is only available to the hostel staff to check the attendance of a particular student
@login_required
def particular_student(request, username):
    try:
        user = User.objects.get(username = request.user)
        hosteladmin = HostelStaff.objects.get(enrollment_id = user)
        try:
            a = get_template("attendance/particular_student.html")
            user = User.objects.get(username = username)
            student = Student.objects.get(enrollment_id = user)
            attend = Attendance.objects.filter(enrollment_id = student)
            c = Context({'attend':attend, 'user':student})
        except:
        # design the except phase differently for hostel staff
            a = get_template("login.html")
            c = Context({})
        html = a.render(c)
        return HttpResponse(html)	
    except :
        return HttpResponse("You dont have enough permissions")
    
@login_required
def daily_attendance(request,year,month,date):
    
    day = year+"-"+month+"-"+date
    daily = Attendance.objects.filter(date = day)
    template = get_template("attendance/daily_attendance.html")
    c = Context({'daily':daily,'date':day})
    html = template.render(c)
    return HttpResponse(html)



