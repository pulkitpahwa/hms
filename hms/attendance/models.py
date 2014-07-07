from django.db import models
from django.contrib.auth.models import User
from profiles.models import Student, Staff, HostelStaff

import datetime

class Holidays(models.Model) : 
    date = models.DateField()

class Outpass(models.Model) :
    permission_choice = (
            ('Y','Yes'),
            ('N','No'),
        )
    outpass_choice = (
            ('W','Waiting'),
            ('P','Processed'),
        )
    save_choice = (
            ('SMS', 'SMS'),
            ('PDF','PDF'),
        )
    enrollment_id  = models.OneToOneField(Student)
    outpass_id = models.AutoField(primary_key = True)
    from_time = models.DateTimeField('Out Time')
    return_time = models.DateTimeField('Expected Return')
    permission_required = models.CharField(max_length = 1, choices = permission_choice) #will be Y if the outpass is not requested on a holiday
    permission_granted_by = models.ManyToManyField(Staff, blank = True, null = True) # will keep a check by whom the permission is granted i.e by which teacher
    permission_granted_by_hostel_staff = models.ManyToManyField(HostelStaff, blank = True, null = True)
    outpass_state = models.CharField(max_length = 2, choices = outpass_choice) #checks whether the output is in waiting state or is generated completely
    outpass_generated = models.DateTimeField("Outpass generated at" ) # fill it in views.py file. WHen the form is completely filled and the outpass could be generated i.e. permission is not required, then outpass_generated = true
    outpass_save_mode = models.CharField(max_length = 3, choices = save_choice) #checks how the outpass is saved i.e. SMS or pdf

#fields to be filled by the user :from_time, to_time 
#fields to be auto-filled in views.py : enrollment_id, outpass_id, permission_required, permission_granted_by, permission_granted_by_hostel_staff, outpass_generated, outpass_save_mode

class Attendance(models.Model):
    present_choice = (
            ('Y',"YES"),
            ('N',"NO"),
        )
    outpass_choice = (
            ('Y',"YES"),
            ('N',"NO"),
            ('NA',"N/A"),
        )
    enrollment_id = models.OneToOneField(User)
    date = models.DateField( default = datetime.date.today)
    present = models.CharField(choices = present_choice, max_length = 2)
    absent = models.CharField(choices = outpass_choice, max_length = 2) 
    outpass = models.CharField(choices = outpass_choice, max_length = 2) 





    # we will read the records from the excel sheet. For every student registered in the hostel, check whether he is present or not, if present, set absent = NA, if present = N, check outpass, if outpass = true, set absent = NO

