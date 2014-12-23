from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='users_avatars')
    rating = models.IntegerField()


class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('User')
    created = models.DateTimeField()
    tags = models.ManyToManyField('Tag')


class Response(models.Model):
    text = models.TextField()
    author = models.ForeignKey('User')
    is_right = models.BooleanField(default=False)


class Tag(models.Model):
    text = models.CharField(max_length=100, unique=True)
