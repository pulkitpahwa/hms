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

sex_choice = (
        ('F','Female'),
        ('M','Male'),
    )

class Person(models.Model):
    enrollment_id = models.OneToOneField(User, primary_key = True)
    name = models.CharField(max_length = 30)
    sex = models.CharField(max_length = 1, choices = sex_choice )
    permanent_address = models.CharField("Permanent address", max_length = 100)  
    city = models.CharField("City", max_length = 30)
    country = models.CharField("Country", max_length = 20)
    email = models.EmailField("Email Address")
    contact = models.CharField("Contact Number", max_length = 12)

    class Meta:
        abstract = True


#the class student, staff and hostel staff extends the class person. This would help them to get those fields automatically. Thus implementing the DRY principle of Python

class Student(Person) :
    course = models.CharField(max_length = 20, choices = course_choice)
    batch = models.CharField(max_length = 4, choices = batch_choice)
    father_name = models.CharField("Father's Name", max_length = 30, blank = True, null = True)
    mother_name = models.CharField("Mother's Name", max_length = 30, blank = True, null = True)
    father_number = models.CharField("Father's Contact Number", max_length = 12)
    mother_number = models.CharField("Mother's Contact Number", max_length = 12)
    local_guardian = models.CharField("Local Guardian's Name", max_length = 30, blank = True, null = True)
    local_guardian_number = models.CharField("Local Guardian's Number", max_length = 12, blank = True, null = True)
    hostel_address = models.CharField("Hostel address", max_length = 5,help_text = "Address format e.g : C441, A221, etc:")
    local_guardian_addres = models.CharField("Local Guardian's Address", max_length = 50, blank = True, null = True)


#Register only HOD, mentors, coordinators and some teachers who stay in hostel or have good terms with students

class Staff(Person):
    branch1 = models.CharField("First Branch I Teach", max_length = 20, choices = course_choice)
    branch2 = models.CharField("Second branch I Teach", max_length = 20, choices = course_choice, blank = True, null = True)
    branch3 = models.CharField("Third branch I Teach", max_length = 20, choices = course_choice, blank = True, null = True)
    address = models.CharField("Current address", max_length = 100)
    position = models.CharField("Current Position", max_length = 20, help_text = "e.g. : HOD, Faculty, etc.")


class HostelStaff(Person):
    address = models.CharField("Hostel address", max_length = 5, help_text = "e.g : A01, B02")
    position = models.CharField("Current Position", max_length = 20, help_text = "e.g. : Warden, Deputy Director Hostel, etc.")


