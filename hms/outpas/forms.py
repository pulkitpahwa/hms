from django import forms
from django.forms import ModelForm
from .models import Outpass
from django.contrib.auth.models import User



class OutpassUpdateForm(ModelForm):
    class Meta:
        model = Outpass
        fields = ('from_date','from_time','return_date','return_time')

#for students
class OutpassCreateForm(ModelForm):
    class Meta:
        model = Outpass
        fields = ('from_date', 'from_time', 'return_date','return_time','going_to','reason', 'description')


