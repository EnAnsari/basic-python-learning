from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def index(request):
    return HttpResponse("Hello, This is my first django Project!")


def postList(request):
    posts = Post.published.all()
    packet = {
        'posts' : posts
    }
    return render(request, 'blog/post/index.html', packet)