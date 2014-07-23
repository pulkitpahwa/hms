from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
    url(r'^all/$',all_outpass),  #only for staff and hostel staff, use pagination, sort by outpass_generated_At
    url(r'^$',my_all_outpass),  #only for student
    url(r'^create/$',CreateOutpass.as_view()),  #only for student
    url(r'^update$',update_outpass),  #only for student
    url(r'^success$',success),  #only for student
    url(r'^failure$',failure),  #only for student
#    url(r'^check$',check),  #only for student
 
)
