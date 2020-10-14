from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'csvmanager/uploader.html', context)

def dashboard(request):
    context = {}
    return render(request, 'csvmanager/uploader.html', context)

def signup(request):
    context = {}
    return render(request, 'csvmanager/signup.html', context)

def signin(request):
    return render(request, 'csvmanager/signin.html')