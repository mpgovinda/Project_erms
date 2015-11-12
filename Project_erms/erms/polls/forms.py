__author__ = 'govinda'

from django import forms
from .models import InfoBasic

class InfoBasicForm(forms.ModelForm):
    class Meta:
        model = InfoBasic
        fields = ['First_name', 'Last_name','Age', 'Email']
