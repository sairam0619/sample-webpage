# myapp/forms.py

from django import forms
from .models import UserSubmission

class UserForm(forms.ModelForm):
    class Meta:
        model = UserSubmission
        fields = ['name', 'email']
