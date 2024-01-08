from django.contrib import admin

from main.models import News, Comment, ContactMessage

admin.site.register(News)
admin.site.register(Comment)
admin.site.register(ContactMessage)
