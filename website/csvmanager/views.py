from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, CSVUploadForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import *
from .decorators import *


# Create your views here.
@login_required(login_url='signin')
def home(request):
    return redirect('dashboard')


@login_required(login_url='signin')
def dashboard(request):
    current_user = request.user
    csvfiles = current_user.csvfile_set.all()
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv = form.save(commit=False)
            csv.uploader = request.user
            csv.csv = request.FILES['csv']
            csv.save()
            return redirect('dashboard')
    else:
        form = CSVUploadForm()
    context = {'CSVs': csvfiles, 'user': current_user, 'form': form}
    return render(request, 'csvmanager/uploader.html', context)


@unauthenticated_user
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
            form = RegistrationForm()
    return render(request, 'csvmanager/signup.html', {'form': form})


@unauthenticated_user
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
