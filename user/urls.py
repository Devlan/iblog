from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('sigup', views.sigup),
    path('login', views.login),

]
