from django import forms
from .models import Business,Profile,Hood,Post,Business,Comment

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','profile','Hood']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','hood','business']

class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude= ['occupants']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','Hood','pub_date']

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['name']
