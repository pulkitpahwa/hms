from django.contrib import admin
from .models import Student, Staff, HostelStaff

class StudentAdmin(admin.ModelAdmin):
    list_display=('enrollment_id', 'name','course','batch','father_number','city')
    list_filter = ['course', 'batch']
    search_fields = ['enrollment_id', 'name', 'course','city','country']


class StaffAdmin(admin.ModelAdmin):
    list_display=('staff_id', 'name','branch1','contact')
    list_filter = ['name', 'batch1']
    search_fields = ['staff_id', 'name', 'branch1']

class StaffAdmin(admin.ModelAdmin):
    list_display=('staff_id', 'name','position','contact')
    list_filter = ['name', 'position']
    search_fields = ['staff_id', 'name', 'position']

admin.site.register(Student, StudentAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(HosteStaff, HostelStaffAdmin)
