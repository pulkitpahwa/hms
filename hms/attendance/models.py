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
    enrollment_id  = models.OneToOneField(Student)
    outpass_id = models.AutoField(primary_key = True)
    from_time = models.DateTimeField('Out Time')
    return_time = models.DateTimeField('Expected Return')
    permission_required = models.CharField(max_length = 1, choices = permission_choice)
    permission_granted_by = models.ManyToManyField(Staff, blank = True, null = True)
    permission_granted_by_hostel_staff = models.ManyToManyField(HostelStaff, blank = True, null = True)
    

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

