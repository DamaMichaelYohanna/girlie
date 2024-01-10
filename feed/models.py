from django.db import models
from user.models import User


class NewsFeed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    images = models.ManyToManyField('NewsFeedImage', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}"


class NewsFeedImage(models.Model):
    image = models.ImageField(upload_to='feed_images/')
