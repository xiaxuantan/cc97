# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class News(models.Model):
	# 新闻标题
    title = models.CharField(max_length=255)
    # 新闻内容
    content = models.TextField()
    # 新闻日期
    publishDate = models.DateTimeField()
    # 新闻源
    source = models.CharField(max_length=255)
    # 浏览数
    scanNumber = models.IntegerField()
    # 评论数
    commentNo = models.IntegerField()
    # 连接
    link = models.CharField(max_length=255)
    # 标签
    tag = models.CharField(max_length=20)
    # 图片连接
    imgLink = models.CharField(max_length=255, default=None)

class Comment(models.Model):
	# 评论者名字
    readerName = models.CharField(max_length=255)
    # 新闻id
    newsId = models.IntegerField()
    # 该新闻第几条评论数
    commentNo = models.IntegerField()
    # 评论内容
    content = models.TextField()
    # 评论日期
    commentDate = models.DateTimeField()