
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    username = models.CharField(max_length =60,primary_key=True)
    user_id = models.IntegerField(default=0)
    hood_id = models.ForeignKey(Hood, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length = 60, null=True)
    profile_picture = models.ImageField(upload_to ='profile/')
    bio = HTMLField()
    
 

    def __str__(self):
        return self.username
    '''save profile method'''
    def save_profile(self):
        self.save()

    '''delete ratings method'''
    def delete_profile(self):
        deleted_profile = Profile.objects.all().delete()
        return deleted_profile

class Hood(models.Model):
    name = models.CharField(max_length = 30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    occupants = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.name

    def create_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def find_hood(cls,hood_id):
        hood = cls.objects.get(id = hood_id)
        return hood

    def update_hood(self):
        self.save()

    def update_occupants(self):
        self.occupants += 1
        self.save()
        


class Business(models.Model):
    username = models.CharField(max_length = 50)
    hood_id= models.ForeignKey(Hood, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 50)
    description = models.TextField(null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
   


    def __str__(self):
        return self.username

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business = Business.objects.get(id = business_id)
        return business

    def update_business(self):
        self.save()

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    hood = models.ForeignKey(NeighbourHood,on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-pub_date']

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.username



class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
