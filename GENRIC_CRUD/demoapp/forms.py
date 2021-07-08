from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Employee
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=Employee
        fields=['username','email','password1','password2']

