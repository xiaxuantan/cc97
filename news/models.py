from __future__ import unicode_literals

from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publishDate = models.DateTimeField()
    source = models.CharField(max_length=255)
    scanNumber = models.IntegerField()
    commentNo = models.IntegerField()
    link = models.CharField(max_length=255)
    tag = models.CharField(max_length=20)
    imgLink = models.CharField(max_length=255, default=None)

class Comment(models.Model):
    readerName = models.CharField(max_length=255)
    newsId = models.IntegerField()
    commentNo = models.IntegerField()
    content = models.TextField()
    commentDate = models.DateTimeField()