from django.contrib import admin
from .models import Hood, UserProfile, Business, Location, Post, Comment, Hospital


# Register your models here.
  

admin.site.register(Hood)
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Hospital)
