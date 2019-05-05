from __future__ import unicode_literals

from django.db import models

from django.utils import timezone


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default=' ')
    pub_date = models.DateTimeField(default=timezone.now)

