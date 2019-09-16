from django import forms
from .models import UserProfile, Business, Hood, Post, Comment, Hospital

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user','hood']

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


# class HospitalForm(forms.ModelForm):
#    class Meta:
#         model = Hospital
#         exclude = ['user', 'hood']