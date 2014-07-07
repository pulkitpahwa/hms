from django.db import models
from django.contrib.auth.models import User

course_choice = (
            ('CSE', "B.Tech CSE"),
            ('ECE', "B.Tech ECE"),
            ('MAE', "B.Tech MAE"),
            ('EEE', "B.Tech EEE"), 
            ('IT', "B.Tech IT"), 
            ('Civil', "B.Tech CIVIL"), 
            ('MBA', "MBA"),
            ('BSCIT', "B.Sc IT"),
            ('BCA', "BCA"),
            ('Biotech', "B.Tech Biotech"),
        )
batch_choice = (
            ('11', "2011"),
            ('12', "2012"),
            ('13', "2013"),
            ('14', "2014"),
            ('15', "2015"),
            ('16', '2016'),
        )

class Student(models.Model) :
    enrollment_id = models.OneToOneField(User, primary_key = True)
    name = models.CharField(max_length = 30)
    course = models.CharField(max_length = 20, choices = course_choice)
    batch = models.CharField(max_length = 4, choices = batch_choice)
    father_name = models.CharField("Father's Name", max_length = 30, blank = True, null = True)
    mother_name = models.CharField("Mother's Name", max_length = 30, blank = True, null = True)
    father_number = models.CharField("Father's Contact Number", max_length = 12)
    mother_number = models.CharField("Mother's Contact Number", max_length = 12)
    local_guardian = models.CharField("Local Guardian's Name", max_length = 30, blank = True, null = True)
    local_guardian_number = models.CharField("Local Guardian's Number", max_length = 12, blank = True, null = True)
    permanent_address = models.CharField("Permanent address", max_length = 50)  
    city = models.CharField("CITY", max_length = 30)
    country = models.CharField("Country", max_length = 20)
    hostel_address = models.CharField("Hostel address", max_length = 5,)
    local_guardian_addres = models.CharField("Local Guardian's Address", max_length = 50, blank = True, null = True)
    email = models.EmailField("Email Address")


#Register only HOD, mentors, coordinators and some teachers who stay in hostel or have good terms with students

class Staff(models.Model):
    staff_id = models.OneToOneField(User)
    name = models.CharField("Name", max_length = 20)
    contact = models.CharField("Contact Number", max_length = 12)
    branch1 = models.CharField("Branch I Teach: First Branch ", max_length = 20, choices = course_choice)
    branch2 = models.CharField("Branch I Teach: Second branch", max_length = 20, choices = course_choice, blank = True, null = True)
    branch3 = models.CharField("Branch I Teach: Third branch", max_length = 20, choices = course_choice, blank = True, null = True)
    address = models.CharField("Current address", max_length = 50)
    position = models.CharField("Current Position", max_length = 20, help_text = "e.g. : HOD, Faculty, etc.")


class HostelStaff(models.Model):
    staff_id = models.OneToOneField(User)
    name = models.CharField("Name", max_length = 20)
    contact = models.CharField("Contact Number", max_length = 12)
    address = models.CharField("Current address", max_length = 50)
    position = models.CharField("Current Position", max_length = 20, help_text = "e.g. : Warden, Deputy Director Hostel, etc.")


