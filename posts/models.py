from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
import datetime

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    post_headline = models.CharField(max_length=256)
    post_description = models.TextField(max_length=4000)
    published_post = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='author')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_headline

    def publish_post(self):
        self.published_post= True
        self.published_date = timezone.now()
        self.save()
    def get_approved_comments(self):
        return self.comments.filter(approved_comment = True)
    def get_absolute_url(self):
        return reverse('index')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=500)
    author_name = models.CharField(max_length=100)
    approved_comment = models.BooleanField(default=False)
    created_date= models.DateTimeField(default=timezone.now)

    def approve_comment(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('index')
