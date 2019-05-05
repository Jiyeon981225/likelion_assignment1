from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def home(request) :
    posts = Post.objects.all
    return render(request, 'blog/home.html', {'posts_list': posts})
