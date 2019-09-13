from django import forms
from .models import Profile, Hood, Business, Post, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user_id']


class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ('username', 'location', 'occupants')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'hood']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'hood']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')