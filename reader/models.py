# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Reader(models.Model):
    #用户名
    readerName = models.CharField(max_length=255)
    #密码
    password = models.CharField(max_length=255)
    #邮箱
    email = models.CharField(max_length=255)
    #头像地址
    icon = models.CharField(max_length=255, default='default.jpeg')
    #性别
    gender = models.CharField(max_length=1,default='M')
    #等级
    level = models.IntegerField(default=0)
    #评论数
    comments = models.IntegerField(default=0)
    #经验值
    exp = models.IntegerField(default=0)
    #升级所需经验值
    levelRatio = models.IntegerField(default=0)
    #注册日期
    registerDate = models.DateTimeField()
    #出生日期
    birthday = models.DateField()