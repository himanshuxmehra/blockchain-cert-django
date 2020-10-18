from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm


# Create your views here.
def home(request):
    context = {}
    return render(request, 'csvmanager/uploader.html', context)


def dashboard(request):
    context = {}
    return render(request, 'csvmanager/uploader.html', context)


def signup(request):
    form_class = RegistrationForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('dashboard')
        else:
            form = UserCreationForm()
    return render(request, 'csvmanager/signup.html', {'form': form})


def signin(request):
    return render(request, 'csvmanager/signin.html')
