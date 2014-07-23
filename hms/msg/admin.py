from django.contrib import admin
from .models import HostelStaffMsg, StaffMsg, SuccessMsg

class HostelStaffMsgAdmin(admin.ModelAdmin):
    list_display = ('outpass','student','hostel_staff','message')
    list_filter = ['student','hostel_staff']
    #search_fields = ['student','hostel_staff']

class StaffMsgAdmin(admin.ModelAdmin):
    list_display = ('outpass','student','staff','message')
    list_filter = ['student','staff']
    #search_fields = ['student','hostel_staff']

class SuccessMsgAdmin(admin.ModelAdmin):
    list_display = ('outpass','student','staff','message')
    list_filter = ['student','staff']
    #search_fields = ['student','hostel_staff']

admin.site.register(HostelStaffMsg, HostelStaffMsgAdmin)
admin.site.register(StaffMsg, StaffMsgAdmin)
admin.site.register(SuccessMsg, SuccessMsgAdmin)
