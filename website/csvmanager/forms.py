from django import forms
from .models import User, CSVFile
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.CharField(
        max_length=200,
        label="Email ...",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control mb-3"
            }
        )

    )
    password1 = forms.CharField(
        label="Password",
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control mb-3"
            }
        )
    )

    password2 = forms.CharField(
        label="Confirm Password",
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control mb-3"
            }
        )
    )
    name = forms.CharField(
        max_length=200,
        label="Name",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Full Name",
                "class": "form-control mb-3"
            }
        )
    )
    university_name = forms.CharField(
        max_length=200,
        label="University Name",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "University Name",
                "class": "form-control mb-3"
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'name', 'university_name')


class CSVUploadForm(forms.ModelForm):
    NETWORK = (
        ('Public', 'Public'),
        ('Private', 'Private')
    )
    csv = forms.FileField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "file-upload-input",
                "type": "file",
                "accept": ".csv",
                "onchange": "readURL(this);",
                "id": "fileUpload"
            }
        )
    )
    network = forms.CharField(
        max_length=200,
        required=False,
        label='Select Blockchain Network',
        widget=forms.Select(
            choices=NETWORK,
            attrs={
                "class": "custom-select",
                "id": "inputGroupSelect01",
                "placeholder": "Select Blockchain Network"
            }
        )
    )
    title = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Title"
            }
        )
    )

    class Meta:
        model = CSVFile
        fields = ['title', 'csv', 'network']
