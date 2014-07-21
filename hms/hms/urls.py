from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from hms import views
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # url(r'^$', 'hms.views.home', name='home'),
    # url(r'^hms/', include('hms.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^outpass/',include('outpas.urls')), 
    url(r'^profile/', include('profiles.urls')), 
    url(r'^attendance/', include('attendance.urls')), 
#    url(r'^(?P<outpass-id>\d{1,5})/(?P<staff-id>\d{1,8})/(?P<enrollment-id>\d{1,8}/$',views.staff_permission_received),  
#    url(r'^(?P<outpass-id>\d{1,5})/girls-hostel/(?P<staff-id>\d{1,8})/(?P<enrollment-id>\d{1,8}/$',views.girls_hostel_staff_permission_received),  
#    url(r'^(?P<outpass-id>\d{1,5})/hostel/(?P<hostel-staff-id>\d{1,8})/(?P<enrollment-id>\d{1,8}/$',views.hostel_staff_permission_received),
)
