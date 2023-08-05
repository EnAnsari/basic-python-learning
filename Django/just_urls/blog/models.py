from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class PostManager(models.Manager):
    def Y(self, year):
        return self.filter(publish__year=year)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    # objects = models.Manager()
    objects = PostManager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug, 'pk': self.id})

    def __str__(self):
        return self.title


class Account(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    phone = models.CharField(max_length=11, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='female')
    address = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    age = models.PositiveIntegerField(default=0, null=True, blank=True)
    # birthday

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {0} on {1}'.format(self.name, self.post)