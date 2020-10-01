from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    return render(request, 'website.html')


def news(request):
    return render(request, 'news.html')


def involved(request):
    return render(request, 'involved.html')

def mission(request):
    return render(request, 'mission.html')


def news1(request):
    return render(request, 'news1.html')


def news2(request):
    return render(request, 'news2.html')


def news2_0(request):
    return render(request, 'news2.0.html')


def news3(request):
    return render(request, 'news3.html')


def news4(request):
    return render(request, 'news4.html')


def news5(request):
    return render(request, 'news5.html')


def news6(request):
    return render(request, 'news6.html')


def news7(request):
    return render(request, 'news7.html')


def news8(request):
    return render(request, 'news8.html')


def news9(request):
    return render(request, 'news9.html')


def news10(request):
    return render(request, 'news10.html')


def news11(request):
    return render(request, 'news11.html')




def Login(request):
    return render(request, 'loinandregisteration.html')

def loginData(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            print('Loged in Successfully')
            return redirect('/')
        else:
            print('Invalid Credentials')
            messages.info(request, 'Invalid Credentials')
            return redirect('/')

    else:
        return redirect('/')

def SignUp(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        firstName = request.POST['firstName']
        CreatUser = User.objects.create_user(first_name=firstName, email=email, username=email, password=password,)
        print('User Created Successfully')
        CreatUser.save()
        return redirect('/')
    else:
        return redirect('/')

def LogOut(request):
    auth.logout(request)
    return redirect('/')

