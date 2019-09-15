from django.contrib import admin
from .models import Hood, User, Business, Location, Post, Comment


# Register your models here.
  

admin.site.register(Hood)
admin.site.register(User)
admin.site.register(Business)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Comment)
