from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from .models import Attendance, Holidays

#I think the update forms are not required here. They might be required in the profiles app. For this app, update attendance option can be available to the staff and faculty members. Update outpass form is required for the student to update the outpass if he/she wants to accomodate the query so as to get the permission without any trouble

#class UserUpdateForm(ModelForm):
#    class Meta:
#        model = User
#        fields = ('first_name', 'last_name', 'email', 'username')


#only available for student

#for staff and faculty
class HolidaysCreateForm(ModelForm):
    class Meta:
        model = Holidays
        fields = ('date_of_holiday','reason')

#for staff and faculty. Only available to selected faculty, but all hostel staff
class HolidaysUpdateForm(ModelForm):
    class Meta:
        model = Holidays
        fields = ('date_of_holiday','reason')


#for hostel staff or faculty
class AttendanceUpdateForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ('enrollment_id', 'date', 'present', 'absent', 'outpass')
