from django.contrib import admin
from .models import Hood, UserProfile, Business, Location, Post, Comment


# Register your models here.
  

admin.site.register(Hood)
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Comment)
