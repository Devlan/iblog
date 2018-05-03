from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('register_handle', views.register_handle),
    path('login_handle', views.login_handle),
    path('upload', views.upload_profile_photo),
    path('center', views.user_center),

]
