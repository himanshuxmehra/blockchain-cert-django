from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='signin')
def home(request):
    context = {}
    return render(request, 'csvmanager/uploader.html', context)


@login_required(login_url='signin')
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
            return redirect('signin')
        else:
            form = UserCreationForm()
    return render(request, 'csvmanager/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'csvmanager/signin.html')


def logoutuser(request):
    logout(request)
    return redirect('signin')
