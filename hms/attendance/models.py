from django.db import models
from django.contrib.auth.models import User
from profiles.models import Student, StaffUser, HostelStaff

import datetime


class Holidays(models.Model) : 
    date_of_holiday = models.DateField('Date')
    reason = models.CharField("Reason for Holiday", max_length = 30)
    
    def __unicode__(self):
        return self.date_of_holiday.strftime("%Y-%m-%d")
    

class Attendance(models.Model):
    outpass_choice = (
            ('Y',"YES"),
            ('N',"NO"),
            ('NA',"N/A"),
        )
    enrollment_id = models.ForeignKey(Student) 
    date = models.DateField(default = datetime.date.today) #to keep a track of the daily date
    present = models.BooleanField(default = False)
    absent = models.BooleanField(default = False)
    outpass = models.CharField(choices = outpass_choice, max_length = 2) #will be selected if the student generates the outpass


    #The field value  of present field in the attendance model will be selected from the values received from the file uploaded by the warden daily. The for loop will access every element of the file and will mark present to all those whose names are present in the file




    # we will read the records from the excel sheet. For every student registered in the hostel, check whether he is present or not, if present, set absent = NA, if present = N, check outpass, if outpass = true, set absent = NO        

