from django.test import TestCase
from django.test import TestCase
from .models import UserProfile,Hood, Business, Post, Comment, Location, Category
from django.contrib.auth.models import User


# Create your tests here.


class UserProfileTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='6789')
        self.profile = UserProfile(id=1, name='sly',user = self.user,bio='test bio')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,UserProfile))

class PostTestClass(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='6789')
        self.post = Post(id=1,title='Test',content='This is a test',user = self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

class CommentTestClass(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='6789')
        self.post = Post(id=1,title='Test',content='This is a test',user = self.user)
        self.comment = Comment(id=1,post=self.post,user=self.user, comment= 'This is a comment')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(id=1,name='Test name
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

class CategoryTestClass(TestCase):

    def setUp(self):
        self.category = Category(id=1,name='Test name')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

class NeighborhoodTestClass(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='6789')
        self.location = Location(id=1,name='Test name')
        self.Hood =Hood(id=1,name='Test name',location=self.location,occupants=1
    def test_instance(self):
        self.assertTrue(isinstance(self.Hood,Hood))

    def test_create_hood(self):
        self.location.save()
        self.Hood.create_hood()
        self.assertTrue(len(Hood.objects.all()) > 0)

    def test_delete_hood(self):
        self.location.save()
        self.Hood.create_hood()
        self.Hood = Hood.objects.get(id=1)
        self.Hood.delete_hood()
        self.assertTrue(len(Hood.objects.all()) == 0)
