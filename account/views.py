from django.contrib import messages
from django.contrib.auth import login as auth_login,logout as auth_logout, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse


def login(request):
    if request.method == "POST":
        username:str = request.POST.get("username")
        password:str = request.POST.get("password")
        print(username, password)
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                print("authenticated")
                return redirect(reverse("main:index"))
            else:
                messages.error(request, "Authentication failed! ")

    return render(request, 'account/login.html')


def logout(request):
    auth_logout(request)
    return redirect(reverse("login"))


def profile(request):
    context = {}
    return render(request, 'account/profile.html', context)


def register(request):
    return render(request, 'account/register.html')
