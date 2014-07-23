from django.db import models

from profiles.models import Student, StaffUser, HostelStaff
from outpas.models import Outpass

class HostelStaffMsg(models.Model):
    message = models.TextField()
    hostel_staff = models.ForeignKey(HostelStaff)
    student = models.ForeignKey(Student)
    outpass = models.ForeignKey(Outpass)

    class Meta :
        ordering = ['outpass',]

class StaffMsg(models.Model):
    message = models.TextField()
    staff = models.ForeignKey(StaffUser)
    student = models.ForeignKey(Student)
    outpass = models.ForeignKey(Outpass)

    class Meta :
        ordering = ['outpass',]


class SuccessMsg(models.Model):
    message = models.TextField()
    staff = models.ForeignKey(HostelStaff)
    student = models.ForeignKey(Student)
    outpass = models.ForeignKey(Outpass)

    class Meta :
        ordering = ['outpass',]


    

