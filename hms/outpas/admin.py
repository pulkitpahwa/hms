from django.contrib import admin
from .models import Outpass

class OutpassAdmin(admin.ModelAdmin):
    list_display=('outpass_id', 'enrollment_id','from_date','from_time','return_date','return_time','outpass_generated','outpass_state')
    list_filter = ['from_date','return_date','outpass_generated']
    search_fields = ['enrollment_id', 'from_time', 'return_time']

admin.site.register(Outpass, OutpassAdmin)
