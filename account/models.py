from django.contrib.auth import get_user_model
from django.db import models


class UserProfile(models.Model):
    user: get_user_model = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    phone_number = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    dob = models.DateField()
    date_joined = models.DateField(auto_created=True)