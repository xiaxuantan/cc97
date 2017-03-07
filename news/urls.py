from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'news/(?P<nid>\d+)', views.news, name='news'),
    url(r'categories/(?P<category>[^/]*)',views.categories,name='categories'),
    url(r'submitComment',views.submitComment,name='submitComment'),
    url(r'(?P<attach>.*)', views.index, name='index'),
]
