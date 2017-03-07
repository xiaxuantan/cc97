# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from reader.models import Reader
from news.models import News, Comment

from django.views.decorators.csrf import csrf_exempt

from datetime import *
import json
# Create your views here.
from django.http import HttpResponse

def index(request, attach):


    print(attach)

    if attach!='':
        return HttpResponseRedirect('/')

    information = {}

    #每天最火的十条
    information['hot'] = News.objects.filter(publishDate__gte=(datetime.now()-timedelta(hours=12,minutes=0,seconds=0)).strftime("%Y-%m-%d %H:%M:%S")).order_by('-scanNumber').all()[0:18]

    if 'readerName' in request.COOKIES:
        readerName = request.COOKIES['readerName']
        reader = Reader.objects.filter(readerName=readerName).first()
        information['reader']=reader
    #else:

    # 最新发布的十条 标题截断
    recentTen = News.objects.order_by('-publishDate').all()[0:10]
    for recent in recentTen:
         if len(recent.title)>=17:
             recent.title = recent.title[0:17]+'...';
    information['recent'] = recentTen
    return render(request, "news/index.html", information)


def news(request, nid):

    # 以后这里换成404
    if nid==0 or nid==None:
        return HttpResponseRedirect('/')

    information = {'newsId':nid}

    #如果没有注册，那没有评论框
    if 'readerName' in request.COOKIES:
        readerName = request.COOKIES['readerName']
        reader = Reader.objects.filter(readerName=readerName).first()
        information['reader']=reader

    oNews = News.objects.filter(id=nid).first()
    #如果新闻ID有误 直接跳转到主页
    if oNews==None:
        return HttpResponseRedirect('/')
    #新闻的访问次数加以
    oNews.scanNumber += 1
    oNews.save()
    #给新闻内容分段
    paragraphs = oNews.content.split('||')
    #取出评论
    comments = Comment.objects.filter(newsId=nid).order_by("commentNo").all()
    information['paragraphs'] = paragraphs
    information['comments'] = comments
    information['news'] = oNews
    return render(request, "news/news.html", information)


@csrf_exempt
def submitComment(request):

    data = request.POST

    content = data['text']

    print(content)

    reader = Reader.objects.filter(readerName=data['readerName']).first()
    reader.exp += 1
    reader.comments += 1

    if reader.level==0:
        reader.levelRatio = int(reader.exp*100.0/10)
    else:
        #计算升级速率
        reader.levelRatio = int((reader.exp-2**(reader.level-1))*10.0/(2**(reader.level-1)*10))

    if reader.exp==(2**reader.level*10):
        reader.level += 1
        reader.levelRatio = 0

    oNews = News.objects.filter(id=data['newsId']).first()
    oNews.commentNo += 1

    comment = Comment(readerName=reader.readerName, newsId=oNews.id,
                      commentNo=oNews.commentNo, content=content, commentDate=datetime.now())

    comment.save()
    oNews.save()
    reader.save()

    return HttpResponse(json.dumps({}),
                        content_type='application/json')

def categories(request, category):

    information = {}

    if 'readerName' in request.COOKIES:
        readerName = request.COOKIES['readerName']
        reader = Reader.objects.filter(readerName=readerName).first()
        information['reader']=reader

    #获取页码
    if request.GET.get('page') is None:
        page = 1
    else:
        page = int(request.GET.get('page'))

    information['tag']=category
    information['page']=page

    if category=='sports':
        information['thisPage']=News.objects.filter(tag='sports').order_by('-publishDate').all()[20*(page-1):20*page]
    elif category=='business':
        information['thisPage'] = News.objects.filter(tag='business').order_by('-publishDate').all()[20*(page-1):20*page]
    elif category=='all':
        information['thisPage'] = News.objects.order_by('-publishDate').all()[
                                  20 * (page - 1):20 * page]

    else:
        return  HttpResponseRedirect('/categories/all')

    return render(request, 'news/category.html', information)