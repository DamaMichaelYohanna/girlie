from django.urls import path

from account import views

urlpatterns = [
    path("login", views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path("profile", views.profile, name="profile"),
    path("register",views.register, name="register")
]