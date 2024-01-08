from django.urls import path
from main import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about_us, name="about_us"),
    path("contact", views.contact_us, name="contact_us"),
    path("news", views.news, name="news"),
    path("news/<str:slug>", views.news_detail, name="news_details"),
    path("mail", views.send_email, name="send mail"),

]