from django.shortcuts import render
from django.conf import settings
import os
from .models import UserInfo

# Create your views here.
def register(request):
    return render(request, 'user/register.html')


def register_handle(request):
    # 从register表单获取用户提交的注册信息
    u_name = request.POST['user_name']
    u_passwd = request.POST['user_passwd']
    u_c_passwd = request.POST['user_confirm_passwd']
    if u_name in UserInfo.user_name:
        print('用户已存在')
    return render(request, 'user/user_center.html')


def login(request):
    return render(request, 'user/user_center.html')


def login_handle(request):
    # 从login表单获取用户提交的注册信息
    u_name = request.POST['user_name']
    u_passwd = request.POST['user_passwd']
    u_c_passwd = request.POST['user_confirm_passwd']
    print(u_passwd, u_name, u_c_passwd)
    return render(request, 'user/login.html')


def upload_profile_photo(request):
    return render(request, 'user/upload_profile_photo.html')


def user_center(request):
    user_photo = request.FILES['user_photo']
    fname = os.path.join(settings.MEDIA_ROOT, user_photo.name)
    with open(fname, 'w') as user_photo:
        user_photo.write()
    return render(request, 'user/user_center.html')
    return render(request, 'user/login.html')
