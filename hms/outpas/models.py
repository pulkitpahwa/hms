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
    from_date = models.DateField('Out Date', help_text = "Date format : YYYY-MM-DD")
    from_time = models.TimeField('Out Time', help_text = "Time Format : HH:MM:SS")
    return_date = models.DateField('Expected Return',help_text = "Date format : YYYY-MM-DD")
    return_time = models.TimeField('Expected Return Time',help_text = "Time Format : HH:MM:SS")
    going_to = models.CharField(max_length = 50)
    reason = models.CharField(max_length = 50)
    girl_permission_required = models.BooleanField() 
    staff_permission_required = models.BooleanField() 
    staff_permission_granted_by = models.ForeignKey(StaffUser, blank = True, null = True)
    permission_granted_by_hostel_staff = models.ForeignKey(HostelStaff, blank = True, null = True)
    outpass_state = models.CharField(max_length = 2, choices = outpass_state)
    outpass_generated = models.DateTimeField()
    outpass_save_mode = models.CharField(max_length = 3, choices = save_choice) #checks how the outpass is saved i.e. SMS or pdf

#    def __unicode__(self):
       # return [self.enrollment_id, self.from_date, self.return_date]


    #The field value  of present field in the attendance model will be selected from the values received from the file uploaded by the warden daily. The for loop will access every element of the file and will mark present to all those whose names are present in the file




    # we will read the records from the excel sheet. For every student registered in the hostel, check whether he is present or not, if present, set absent = NA, if present = N, check outpass, if outpass = true, set absent = NO


        #1. Girls need permission everytime they want to generate the outpass
        #2. Boys need permission only if they are leaving for many days,or the days when they would be missing is a working day or has some event
        
        

