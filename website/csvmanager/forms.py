from django import forms
from .models import User

class RegistrationForm(forms.Form):
    email = forms.CharField(max_length=200, label="Email ...")
    password = forms.CharField(max_length=255, label="Password")
    name = forms.CharField(max_length=200, label="Name")
    university_name = forms.CharField(max_length=200, label="University Name")

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         field = ('email', 'password', 'name', 'university_name')