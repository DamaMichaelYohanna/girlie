from django.contrib import admin

from user.models import User, Relationship

admin.site.register(User)
admin.site.register(Relationship)
