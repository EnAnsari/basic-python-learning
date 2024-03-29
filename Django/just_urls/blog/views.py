from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count, Q
from django.db.models.functions import Greatest
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from taggit.models import Tag

from .forms import AccountForm, ShareForm, CommentForm, LoginForm, ChangePasswordForm
from .models import Post, Account


def index(request):
    return HttpResponse("Hello, This is my first django Project!")


def postList(request, tag_slug=None):
    posts = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    packet = {
        'posts': posts,
        'page': page,
        'tag': tag,
    }
    return render(request, 'blog/post/index.html', packet)


# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 2
#     template_name = 'blog/post/index.html'


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

    ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(s_count=Count('tags')).order_by('-s_count', '-publish')[:2]

    packet = {
        'post': post,
        'cm': comments,
        'ncm': new_comment,
        'cm_form': comment_form,
        'similar_posts': similar_posts,
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


def regroup(request):
    packet = [
        {'name': 'Rahmat', 'age': 21, 'weight': 80},
        {'name': 'Amir', 'age': 14, 'weight': 60},
        {'name': 'Reza', 'age': 50, 'weight': 90},
        {'name': 'Hossein', 'age': 21, 'weight': 70},
        {'name': 'Narges', 'age': 14, 'weight': 50},
    ]
    text = "Hello"
    return render(request, 'blog/post/regroup.html', {'packet': packet, 'text': text})


def search(request):
    if request.method == 'GET':
        query_name = request.GET.get('search-input')
        if query_name:
            request.session['query-session'] = query_name
        else:
            try:
                query_name = request.session['query-session']
            except:
                query_name = ''

        # result1 = Post.published.filter(body__search=query_name)
        # search_vector = SearchVector('body', weight='B') + SearchVector('title', weight='A')
        # search_query = SearchQuery(query_name)
        # search_rank = SearchRank(search_vector, search_query)
        # posts = Post.published.annotate(
        #     # search=search_vector,
        #     rank=search_rank
        # ).filter(rank__gte=0.3).order_by('-rank')

        # posts = Post.published.filter(Q(body__contains=query_name) | Q(title__contains=query_name))

        sim_search = Greatest(
            TrigramSimilarity('body', query_name),
            TrigramSimilarity('title', query_name)
        )
        posts = Post.published.annotate(sim=sim_search).filter(sim__gt=0.0).order_by('-sim')
        paginator = Paginator(posts, 2)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'blog/post/index.html', {'posts': posts, 'page': page})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:index')
                else:
                    return HttpResponse('Your Account is de-active!')
            else:
                return HttpResponse('username or password is incorrect!')
    else:
        form = LoginForm()
    return render(request, 'blog/forms/account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home:index')


@login_required(login_url='home:index')
def change_password(request):
    if request.method == 'POST':
        user = request.user
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            old_password = cd['old_password']
            new_password1 = cd['new_password1']
            new_password2 = cd['new_password2']
            if not user.check_password(old_password):
                return HttpResponse('your old password is incorrect!')
            elif new_password1 != new_password2:
                return HttpResponse('your new passwords is not equal!')
            else:
                user.set_password(new_password1)
                user.save()
                login(request, user)
                # return HttpResponse('your password is changed successfully!')
                return redirect('home:index')
    else:
        form = ChangePasswordForm()
    return render(request, 'blog/forms/account/change_password.html', {'form': form})