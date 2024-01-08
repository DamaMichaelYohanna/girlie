from django.contrib.auth.views import auth_login, auth_logout
from django.shortcuts import render, redirect
from django.urls import reverse


def login(request):
    return render(request, 'account/login.html')


def logout(request):
    auth_logout(request)
    return redirect(reverse("login"))


def profile(request):
    context = {}
    return render(request, 'account/profile.html', context)


def register(request):
    return render(request, 'account/register.html')
