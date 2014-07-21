from django.db import models
from django.contrib.auth.models import User
import datetime

from profiles.models import Student, StaffUser, HostelStaff

class Outpass(models.Model) :
    outpass_state = (
            ('W','Waiting'),
            ('P','Processed'),
        )
    save_choice = (
            ('SMS', 'SMS'),
            ('PDF','PDF'),
        )
    enrollment_id  = models.ForeignKey(Student)
    outpass_id = models.AutoField(primary_key = True)
    from_date = models.DateField('Out Date')
    from_time = models.TimeField('Out Time')
    return_date = models.DateField('Expected Return')
    return_time = models.TimeField('Expected Return Time')
    going_to = models.CharField(max_length = 50)
    reason = models.CharField(max_length = 50)
    girl_permission_required = models.BooleanField() 
    staff_permission_required = models.BooleanField() 
    staff_permission_granted_by = models.ForeignKey(StaffUser, blank = True, null = True)
    permission_granted_by_hostel_staff = models.ForeignKey(HostelStaff, blank = True, null = True)
    outpass_state = models.CharField(max_length = 2, choices = outpass_state)
    outpass_generated = models.DateTimeField(datetime.datetime.now())
    outpass_save_mode = models.CharField(max_length = 3, choices = save_choice) #checks how the outpass is saved i.e. SMS or pdf

    def is_permission_required(self):
        permission = check_date(from_date,from_time, return_date, return_time)
        return permission


    #function to check whether the girl permission is required. If the girl permission is required, outpass_state = waiting state
    def is_girl_permission_required(self):
        if enrollment_id.sex == 'F':
            message = "Permission is required from the warden for you to be eligible to generate your outpass. Please contact your warden."
            self.outpass_state = "W"


    def __unicode__(self):
        return [self.enrollment_id, self.from_date, self.return_date]

#fields to be filled by the user :from_time, to_time 
#fields to be auto-filled in views.py : enrollment_id, outpass_id, permission_required, permission_granted_by, permission_granted_by_hostel_staff, outpass_generated, outpass_save_mode


    #The field value  of present field in the attendance model will be selected from the values received from the file uploaded by the warden daily. The for loop will access every element of the file and will mark present to all those whose names are present in the file




    # we will read the records from the excel sheet. For every student registered in the hostel, check whether he is present or not, if present, set absent = NA, if present = N, check outpass, if outpass = true, set absent = NO


        #1. Girls need permission everytime they want to generate the outpass
        #2. Boys need permission only if they are leaving for many days,or the days when they would be missing is a working day or has some event
        
        

