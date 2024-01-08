from django.contrib.auth import get_user_model
from django.db import models


class ContactMessage(models.Model):
    """models for messages to be received from the users"""
    full_name = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.full_name}"


class News(models.Model):
    """model for news to"""
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateField(auto_created=True)
    image = models.ImageField(upload_to='uploads/')
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    posted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    """model for comment associated with news model"""
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user}"
