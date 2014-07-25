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
#        from_date = forms.DateField(required=True, label='Out Date',help_text='Date Format : YYYY-MM-DD')
#        from_time = forms.TimeField(required=True, label='Out Time',help_text='Time Format : HH-MM-SS')
#        return_date = forms.DateField(required=True, label='Return Date',help_text='Date Format : YYYY-MM-DD')
 #       return_time = forms.TimeField(required=True, label='Return Time',help_text='Time Format : HH-MM-SS')
        fields = ('from_date', 'from_time', 'return_date','return_time','going_to','reason','outpass_save_mode')


