
from django import forms
from .models import User, Business, Hood, Post, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['user','']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'hood']

class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ('name', 'location', 'occupants')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'hood']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)