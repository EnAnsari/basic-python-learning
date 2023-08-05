from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Account, Comment
from .forms import AccountForm, ShareForm, CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.core.mail import send_mail

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


def postdetail(request, slug, pk):
    post = get_object_or_404(Post, status='published', slug=slug, id=pk)
    # comments = Comment.objects.filter(post=post)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    packet = {
        'post': post,
        'cm': comments,
        'ncm': new_comment,
        'cm_form': comment_form,
    }
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
            account.age = form.cleaned_data['age']
            account.phone = form.cleaned_data['phone']
            user.save()
            account.save()
            return redirect('blog:index')
        else:
            return render(request, 'blog/forms/account_form.html', {'form': form, 'account': account})
    form = AccountForm()
    return render(request, 'blog/forms/account_form.html', {'form': form, 'account': account})


def sharePost(request, post_id):
    post = get_object_or_404(Post, status='published', id=post_id)
    sent = False
    if request.method == 'POST':
        form = ShareForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{0} invited you to read {1}'.format(cd['name'], post.title)
            to = cd['to']
            message = cd['message']
            msg = f"{cd['name']} invited you to reading {post.title} post in above link:\n{post_url}\n{message}"
            from_email = 'en.ansari@outlook.com'
            sent = send_mail(subject, msg, from_email, [to], fail_silently=True)
            return render(request, 'blog/forms/share-post.html', {'form': form, 'sent': sent, 'post': post})
    form = ShareForm()
    return render(request, 'blog/forms/share-post.html', {'form': form, 'sent': sent, 'post': post})