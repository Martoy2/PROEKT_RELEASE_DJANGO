from django.shortcuts import render, redirect
from .forms import AuthForm, ProfileImage
from django.contrib.auth import login, authenticate
from .models import NewUser, Course
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage



def signup(request):
    error = ''
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            email = form.data['email']
            password = form.data['password']
            user = NewUser.objects.create_user(email=email, password=password)
            login(request, user)
            return redirect('home')
        else:
            error = ValueError('Почта уже занята')
    form = AuthForm()
    context={
        'form': form,
        'error': error,
    }
    return render(request, 'main/signup.html', context)


def LoginForm(request):
    error = ''
    if request.method == 'POST':
        form = AuthForm(request.POST)
        email = form.data['email']
        password = form.data['password']
        user = authenticate(email=email, password=password)
        email = NewUser.objects.filter(email=user)
        for subscribe_date in email:
            subscribe_date = subscribe_date.subscribe_date
        now=datetime.now()
        if subscribe_date < datetime.date(now):
            for subscribe in email:
                subscribe = subscribe.subscribe
            NewUser.objects.filter(subscribe=subscribe).update(subscribe="DEFAULT")
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = ValueError('Такого аккаунта не сущетсвует')

    form = AuthForm()
    context={
        'form': form,
        'error': error,
    }
    return render(request, 'main/login.html', context)


def profile(request):
    if request.method == 'POST':
        form = ProfileImage(request.FILES, request.POST)
        if form.is_valid():
            pass
    form = ProfileImage
    context = {
        'form': form
        }
    return render(request, 'main/profile.html', context)


def courses(request):
    courses = Course.objects.order_by('-date')
    context = {
        'courses': courses,
    }
    return render(request, 'main/courses.html', context)
