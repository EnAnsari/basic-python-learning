from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('postlist/', views.postList, name='post_list'),
    path('postlist/<slug:tag_slug>/', views.postList, name='post_list_tag'),
    # path('postlist/', views.PostListView.as_view(), name='post_list'),
    path('postdetail/<slug:slug>/<int:pk>/', views.postdetail, name='post_detail'),
    path('account-form/', views.userAccount, name='account_form'),
    path('share-post/<int:post_id>/', views.sharePost, name='share-post'),
    path('regroup/', views.regroup, name='regroup'),
    path('search/', views.search, name='search'),
    path('login/', views.user_login, name='login'),
]