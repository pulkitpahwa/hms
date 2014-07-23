from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
    url(r'^$',my_attendance),  #only for student
    url(r'^(?P<year>\d{1,4})/(?P<month>\d{1,2})/(?P<date>\d{1,2})/$',daily_attendance),  #only for hostel_staff
    url(r'^user/(?P<username>\d{1,7})$',particular_student),  #only for hostel_staff # to check the attendance of a particular student

#    url(r'^add/$',add_attendance),  #only for hostel_staff
# THE ABOVE URL HANDLES THE UPLOADED CSV OR EXCEL FILE AND PROCESS IT TO UPLOAD ATTENDANCE

#    url(r'^(?P<year>\d{4,4})-(?P<month>\d{4,4})-(?P<date>\d{4,4}/(?P<username>\d{1,7}/update)$',update_attendance),  #only for hostel_staff     to update the attendance of a particular student
)
