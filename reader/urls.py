# -*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    # 暴露给外界的api
    url(r'space/(?P<readerName>\w+)', views.space, name='space'),
    url(r'^session', views.session, name='session'),
    url(r'^fresher', views.fresher, name='fresher'),
    url(r'^profileUpdate', views.profileUpdate, name='profileUpdate'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^passwordUpdate', views.passwordUpdate, name='passwordUpdate'),
    url(r'^uploadIcon', views.uploadIcon, name='uploadIcon'),
    url(r'^updateIcon', views.updateIcon, name='updateIcon'),
]
