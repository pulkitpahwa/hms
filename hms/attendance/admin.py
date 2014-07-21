from django.contrib import admin
from .models import Holidays, Attendance

class HolidayAdmin(admin.ModelAdmin):
    pass

#class OutpassAdmin(admin.ModelAdmin):
#    list_display=('outpass_id', 'enrollment_id','from_time','return_time','outpass_generated','outpass_state')
#    list_filter = ['enrollment_id', 'from_time','return_time','outpass_generated']
#    search_fields = ['enrollment_id', 'from_time', 'return_time']
#    pass

class AttendanceAdmin(admin.ModelAdmin):
    list_display=('date', 'enrollment_id' ,'present','absent','outpass')
    list_filter = ['enrollment_id','date']
    search_fields = ['enrollment_id', 'date']


admin.site.register(Holidays, HolidayAdmin)
admin.site.register(Attendance, AttendanceAdmin)
