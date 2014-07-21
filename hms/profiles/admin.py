from django.contrib import admin
from .models import Student, StaffUser, HostelStaff

class StudentAdmin(admin.ModelAdmin):
    list_display=('enrollment_id', 'name','course','batch','father_number','city')
    list_filter = ['course', 'batch']
    search_fields = ['enrollment_id', 'name', 'course','city','country']

class StaffUserAdmin(admin.ModelAdmin):
    list_display=('enrollment_id', 'name','branch1','contact')
    list_filter = ['name', 'branch1']
    search_fields = ['enrollment_id', 'name', 'branch1']

class HostelStaffAdmin(admin.ModelAdmin):
    list_display=('enrollment_id', 'name','position','contact')
    list_filter = ['name', 'position']
    search_fields = ['enrollment_id', 'name', 'position']


admin.site.register(Student, StudentAdmin)
admin.site.register(StaffUser, StaffUserAdmin)
admin.site.register(HostelStaff, HostelStaffAdmin)
