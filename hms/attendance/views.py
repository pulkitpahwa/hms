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
from braces.views import SetHeadlineMixin

from .models import Attendance, Holidays
from .forms import HolidaysCreateForm, HolidaysUpdateForm, AttendanceUpdateForm

from django.contrib.auth.decorators import login_required

# must check elements in the templates, if enrollment_id.sex = F, display the column of permission received from the warden column in the status of outpass. And other features

min_out_time = datetime.time(15,00,00)
max_in_time  = datetime.time(10,00,00)

#make sure to call this function if any change is made to the holidays object. In short call this inside the update holidays class and create holidays class
def update_holidays():
    holiday = Holidays.objects.all()
    list_holidays = []
    for day in holiday :
        list_holiday.append(day.date.strftime("%Y-%m-%d"))



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

###########################

@login_required
def my_attendance(request):
    a = get_template("index.html")
    enrollment_id = request.GET['username']
    c = Context({'user':enrollment_id})
    html = a.render(c)
    return HttpResponse(html)	



