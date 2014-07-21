from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
    url(r'^$',view_profile),  #for student, hostel-staff and staff
    url(r'^add/$',edit_profile),  #for hostel_staff, staff and students

)
