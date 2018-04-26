from django.shortcuts import render


# Create your views here.
def register(request):
    return render(request, 'user/register.html')


def login(request):
    return render(request, 'user/login.html')


def sigup(request):
    user_name = request.POST['user_name']
    user_passwd = request.POST['user_passwd']
    user_email = request.POST['user_email']
    context = {'user_name': user_name, 'user_passwd': user_passwd, 'user_email': user_email}
    return render(request, 'user/sigup.html', context)
