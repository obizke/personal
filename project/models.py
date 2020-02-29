from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from tinymce import HTMLField


class Jwear(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(default='default.jpeg', upload_to='staff/')

    def __str__(self):
        return f'{self.user.username} Author'


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blog/')
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey(Jwear, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class ProductCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Item(models.Model):
    STATUS_CHOICES = (
        ('featured', 'Featured'),
        ('newproduct', 'New product'),
        ('inspired', 'Inspired'),
    )

    title = models.CharField(max_length=100)
    category = models.ManyToManyField(ProductCategory)
    price = models.FloatField()
    image = models.ImageField(upload_to='clothes/')
    availability = models.BooleanField(default=True)
    descriptions = models.TextField()
    quantity = models.IntegerField(default=0)
    discount = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inspired')

    def __str__(self):
        return self.title
