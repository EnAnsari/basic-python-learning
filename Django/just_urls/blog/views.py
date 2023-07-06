from django.shortcuts import render, get_object_or_404
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


def postdetail(request, year, month, day, post):
    post2send = get_object_or_404(Post, status='published', publish__year=year, publish__month=month, publish__day=day, slug=post)
    packet = {'post': post2send}
    return render(request, 'blog/post/postdetail.html', packet)