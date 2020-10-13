from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('test/', views.test),
    path('signup', views.signup),
    path('signin', views.signin),
]
