from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
    url(r'^$',view_profile),  #for student, hostel-staff and staff
    url(r'^add/$',StudentCreateView.as_view()),  #for hostel_staff, staff and students
    #not working
    url(r'^(?P<pk>[^/]+)/update/$',StudentUpdateView.as_view()),  #for hostel_staff, staff and students


)
