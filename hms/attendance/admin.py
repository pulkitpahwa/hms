from django.contrib import admin
from .models import Holidays, Attendance

class HolidayAdmin(admin.ModelAdmin):
    list_display=('date_of_holiday', 'reason')

class AttendanceAdmin(admin.ModelAdmin):
    list_display=('date', 'enrollment_id' ,'present','absent','outpass')
    list_filter = ['enrollment_id','date']
    search_fields = ['enrollment_id', 'date']


admin.site.register(Holidays, HolidayAdmin)
admin.site.register(Attendance, AttendanceAdmin)
