from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

class UserLoginForm(forms.Form):
    """Form to login user"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
