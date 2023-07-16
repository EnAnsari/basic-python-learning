from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    # path('postlist/', views.postList, name='post_list'),
    path('postlist/', views.PostListView.as_view(), name='post_list'),
    path('postdetail/<int:year>/<int:month>/<int:day>/<slug:post>/', views.postdetail, name='post_detail'),
    path('account-form/', views.userAccount, name='account_form'),
]