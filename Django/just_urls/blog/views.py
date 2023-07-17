from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Account
from .forms import AccountForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView


# Create your views here.


def index(request):
    return HttpResponse("Hello, This is my first django Project!")


# def postList(request):
#     posts = Post.published.all()
#     paginator = Paginator(posts, 2)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     packet = {
#         'posts': posts,
#         'page': page,
#     }
#     return render(request, 'blog/post/index.html', packet)

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/index.html'


def postdetail(request, year, month, day, post):
    post2send = get_object_or_404(Post, status='published', publish__year=year, publish__month=month, publish__day=day,
                                  slug=post)
    packet = {'post': post2send}
    return render(request, 'blog/post/postdetail.html', packet)


def userAccount(request):
    user = request.user
    try:
        account = Account.objects.get(user=user)
    except:
        account = Account.objects.create(user=user)
    if request.POST:
        form = AccountForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            account.gender = form.cleaned_data['gender']
            account.address = form.cleaned_data['address']
            user.save()
            account.save()
            return redirect('blog:index')
        else:
            return render(request, 'blog/forms/account_form.html', {'form': form, 'account': account})
    form = AccountForm()
    return render(request, 'blog/forms/account_form.html', {'form': form, 'account': account})
