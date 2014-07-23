from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
    url(r'^$',view_profile),  #for student, hostel-staff and staff
    url(r'^add/$',StudentCreateView.as_view()),  #for hostel_staff, staff and students
    # the following link is not working. error of pk
    url(r'^(?P<pk>[^/]+)/update/$',StudentUpdateView.as_view()),  #for hostel_staff, staff and students


)
