from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from user.models import User, OTP


def login(request):
    if request.method == "POST":
        username: str = request.POST.get("username")
        password: str = request.POST.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                messages.success(request, "Login Success")
                return redirect(reverse("user:dashboard"))
            else:
                messages.error(request, "Authentication failed! ")

    return render(request, 'account/login.html')


def logout(request):
    auth_logout(request)
    return redirect(reverse("login"))


def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if username and password:
            try:
                user: User = User.objects.create(username=username)
                user.set_password(password)
                if email:
                    user.email = email
                user.save()
            except IntegrityError:
                messages.error(request, "Username Already exist")
            else:
                if email:
                    # send welcoming email to the user
                    msg_from: str = "get2dama11@gmail.com"
                    msg_to: str = user.email
                    msg_body: str = "Registration successfully. Welcome to Girlie"
                    send_mail(subject="Registration Successful",
                              message=msg_body, from_email=msg_from,
                              recipient_list=[msg_to],
                              )
                messages.success(request, "Registration successful")
                return redirect(reverse("user:dashboard"))

    return render(request, 'account/register.html')


def verify_email(request, otp):
    """function to verify user email using otp
        that has be sent to their email."""
    otp_object: OTP = get_object_or_404(OTP, code=otp)
    otp_object.user.email_verified = True
    otp_object.save()
    otp_object.delete()
    return redirect(reverse("user:dashboard"))


@login_required()
def profile(request):
    return render(request, 'account/base_dashboard.html1')


def dashboard(request):
    return render(request, 'account/base_dashboard.html')


@login_required()
def follow_user(request, username):
    current_user: User = request.user
    new_user: User = User.objects.get(username=username)
    current_user.follow(new_user)
    return redirect(reverse("user:dashboard"))


@login_required()
def unfollow_user(request, username):
    current_user: User = request.user
    new_user: User = User.objects.get(username=username)
    current_user.unfollow(new_user)
    return redirect(reverse("user:dashboard"))


@login_required()
def block_user(request, username):
    current_user: User = request.user
    other_user: User = User.objects.get(username=username)
    current_user.block_user(other_user)
    return redirect(reverse("user:dashboard"))


def unblock_user(request, username):
    current_user: User = request.user
    other_user: User = User.objects.get(username=username)
    current_user.unblock_user(other_user)
    return redirect(reverse("user:dashboard"))
