from django.urls import path

from user import views

urlpatterns = [
    path("login", views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path("register",views.register, name="register"),
    path("verify/<uuid:otp>", views.verify_email, name="verify_email"),
    path("profile", views.profile, name="profile"),
    path("dashboard", views.dashboard, name="dashboard"),
    # --------------------------------------------------
    path("follow/<str:username>", views.follow_user, name="follow"),
    path("unfollow/<str:username>", views.unfollow_user, name="unfollow"),
    path("block/<str:username>", views.block_user, name="block"),
    path("unblock/<str:username>", views.unblock_user, name="unblock"),

]
app_name = "user"
