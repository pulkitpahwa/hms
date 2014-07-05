from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=('enrollment_id', 'name','course','batch','father_number','city')
    list_filter = ['course', 'batch']
    search_fields = ['enrollment_id', 'name', 'course','city','country']

admin.site.register(Student, StudentAdmin)

