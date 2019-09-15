
from django.shortcuts import render, redirect
from .models import Business, User, Hood, Post, Comment
from .forms import ProfileForm, BusinessForm, HoodForm, PostForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login')
def index(request):
    current_user = request.user
    try:
        profile = User.objects.get(user = current_user)
    except:
        profile = User.objects.create(name = request.user.username, user = request.user)
        profile.save()
        return redirect('edit_profile',username = current_user.username)

    posts = Post.objects.filter(hood = profile.hood)
    business = Business.objects.filter(hood = profile.hood)
    hood = profile.hood

    context = {
        "post":post,
        "profile":profile, 
        "business": business, 
        "hood": hood
    }

    return render(request,'index.html', context)

@login_required(login_url='/accounts/login')
def search(request):
    if 'business' in request.GET and request.GET['business']:
        profile = UserProfile.objects.get(user = request.user)
        search_term = request.GET.get('business')
        results = Business.objects.filter(hood = profile.hood, name__icontains = search_term)
        message = f'{search_term}'
        context = {
            'message': message,
            'results': results
        }
        
    return render(request, 'search.html', context)

@login_required(login_url='/accounts/login')
def business(request):
    profile = User.objects.get(user = request.user)
    businesses = Business.objects.filter(hood = profile.hood)
    context = {
        'businesses': businesses
    }    
    return render(request, 'business.html', context)

@login_required(login_url='/accounts/login')
def post(request, id):
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post = post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return redirect('post', id)
    else:
        form = CommentForm()
    context = {
        'post': post,
        'form': form,
        'comments': comments
    }    
    return render(request, 'post.html', context)
    
@login_required(login_url='/accounts/login')
def profile(request, username):
    user = User.objects.get(username = username)
    profile = UserProfile.objects.get(user = user)
    businesses = Business.objects.filter(user = profile)
    context = {
        'profile': profile,
        'businesses': businesses
    }
    return render(request, 'profile.html', context)

@login_required(login_url='/accounts/login')
def edit_profile(request,username):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        return redirect('profile', username = request.user)
    else:
        if UserProfile.objects.filter(user=request.user):
            profile = UserProfile.objects.get(user=request.user)
            form = ProfileForm(instance=profile)
        else:
            form = ProfileForm()
    context = {
        "form":form
    }
    return render(request,'edit_profile.html',context)

@login_required(login_url='/accounts/login')
def new_post(request):
    profile = UserProfile.objects.get(user = request.user)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.neighbourhood = profile.neighbourhood
            post.save()
        return redirect('index')
    else:
        form = PostForm()
    context = {
        "profile":profile,
        "form":form
    }
    return render(request,'new_post.html', context)

@login_required(login_url='/accounts/login')
def new_business(request):
    profile = UserProfile.objects.get(user = request.user)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = profile
            business.hood = profile.hood
            business.save()
        return redirect('business')
    else:
        form = BusinessForm()
    context = {
        'form': form
    }
    return render(request, 'new_business.html', context)