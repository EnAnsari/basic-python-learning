from django import template
from ..models import Post
import datetime
from django.template.defaultfilters import upper
import markdown
from django.utils.safestring import mark_safe

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


@register.filter(name='rep')
def replace_dash(text, sep='-'):
    return upper(str(text).replace(' ', sep))


@register.filter(name='markdown')
def markdown_filter(text):
    if 'script' not in text:
        return mark_safe(markdown.markdown(text))
    return 'No Text!'