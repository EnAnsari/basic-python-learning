from django import template
from ..models import Post
import datetime

register = template.Library()


@register.simple_tag(name='numOfPosts')
def number_of_posts(is_today=False):
    if is_today:
        today = datetime.date.today()
        return Post.published.filter(publish__year=today.year, publish__month=today.month, publish__day=today.day).count()
    return Post.published.count()


@register.inclusion_tag('blog/post/last-posts.html')
def last_posts(count=3):
    posts = Post.published.order_by('-publish')[:count]
    return {'posts': posts}