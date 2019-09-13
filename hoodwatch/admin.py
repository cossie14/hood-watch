from django.contrib import admin
from .models import Business, hood,Profile,Post
admin.site.register(hood)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Business)