from django.db import models
from django.core import urlresolvers
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='users_avatars')
    rating = models.IntegerField()


class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('User', related_name='questions')
    created = models.DateTimeField()
    tags = models.ManyToManyField('Tag', related_name='questions')

    def get_absolute_url(self):
        return urlresolvers.reverse('question', kwargs={'pk': self.pk})


class Response(models.Model):
    text = models.TextField()
    author = models.ForeignKey('User', related_name='responses')
    question = models.ForeignKey('Question', related_name='responses')
    is_right = models.BooleanField(default=False)


class Tag(models.Model):
    text = models.CharField(max_length=100, unique=True)
