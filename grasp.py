# -*- coding:utf-8 -*-


import MySQLdb
import sys
from bs4 import BeautifulSoup
import urllib2
import re
import random

def grasp_hupu():

    reload(sys)
    sys.setdefaultencoding('utf8')

    rawdata = urllib2.urlopen('http://www.hupu.com').read()

    soup = BeautifulSoup(rawdata,'lxml')
    #print(type(soup))
    headerHtml = str(soup.select('.focusNews')[0])

    pattern = re.compile(r'https://voice[\w\./]*html')

    pageLinks = pattern.findall(headerHtml)

    db = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="CC97",port=3306,charset="utf8")
    cursor = db.cursor()




    if pageLinks:

        f = open('newsUpdate.sql','w')

        f.write('use CC97;\n')

        for link in pageLinks:

            print(link)

            pageHtml = urllib2.urlopen(link).read()
            soup = BeautifulSoup(pageHtml,'lxml')

            article = soup.select('.artical-main-content')[0]
           # print(comments)
            passage = ''
            for child in article.children:
                if str(type(child))=="<class 'bs4.element.Tag'>":
                    if child.name=='p' or child.name=='span':
                        try:
                            passage += child.string+"||"
                        except:
                            True

            imgLink = soup.select('.artical-importantPic')[0].contents[1].attrs['src']

            createTime = soup.find_all('meta', {'name':'weibo:webpage:create_at'},limit=3)[0].attrs['content']+":00"
            #2017-03-05 22:55
            title = soup.select('.headline')[0].string.strip()
            scanNumber = int(soup.select('.btn-viewComment')[0].contents[-1].string.strip())*1234
            #print(scanNumber)
            #print(createTime)
            #print(title)
            sql = "insert into news_news(title, content, publishDate, scanNumber, source, commentNo, link, tag, imgLink) " \
                  "values (\'%s\',\'%s\',\'%s\',%d,\'%s\',0,\'%s\',\'%s\',\'%s\');\n" \
                  % (title, passage, createTime, scanNumber, "虎扑", link, 'sports',imgLink)
            # try:
            #     # 执行sql语句
            #     cursor.execute(sql)
            #     # 提交到数据库执行
            #     db.commit()
            # except:
            #     # 发生错误时回滚
            #     db.rollback()
            try:
                cursor.execute(sql)
            except:
                'do nothing'

            f.write(sql);

        db.commit()
        db.close()
        f.close()

def grasp_tencent_finance():
    reload(sys)
    sys.setdefaultencoding('utf8')

    mainHtml = []
    while len(mainHtml) == 0:
        rawdata = urllib2.urlopen('http://finance.qq.com').read()
        soup = BeautifulSoup(rawdata, 'lxml')
        mainHtml = soup.select('.yaowen')

    mainHtml = str(mainHtml[0])

    #print(mainHtml)

    pattern = re.compile(r'http://finance.qq.com/a/\d+/\d+\.htm')
   # pattern = re.compile(r'https://voice[\w\./]*html')

    pageLinks = pattern.findall(mainHtml)

    linksSet = set()

    for link in pageLinks:
        linksSet.add(link)

    pageLinks = list(linksSet)

    db = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="CC97", port=3306, charset="utf8")
    cursor = db.cursor()

    f = open('newsUpdate.sql', 'w')

    f.write('use CC97;\n')

    for link in pageLinks:

        print link
        pageHtml = urllib2.urlopen(link).read()
        soup = BeautifulSoup(pageHtml, 'lxml')


        article = soup.select('#Cnt-Main-Article-QQ')

        if len(article)==0:
            continue
        else:
            article = article[0]

        passage = ''

        for child in article.children:
            if str(type(child)) == "<class 'bs4.element.Tag'>":
                if child.name == 'p': #or child.name == 'span':
                    try:
                        passage += child.string + "||"
                    except:
                        True

        title = soup.title.string.split('_')[0]
        createTime = soup.select('.a_time')[0].string+":00"
        scanNumber = (random.random()*10000)+12000

        sql = "insert into news_news(title, content, publishDate, scanNumber, source, commentNo, link, tag, imgLink) " \
              "values (\'%s\',\'%s\',\'%s\',%d,\'%s\',0,\'%s\',\'%s\',\'%s\');\n" \
              % (title, passage, createTime, scanNumber, "腾讯", link, 'business', '')
        f.write(sql)
        try:
            cursor.execute(sql)
        except:
            'do nothing'

    db.commit()
    db.close()
    f.close()

def grasp_guokr_tech():

    reload(sys)
    sys.setdefaultencoding('utf8')

    rawdata = urllib2.urlopen('https://www.guokr.com/scientific/subject/internet/').read()

    soup = BeautifulSoup(rawdata, 'lxml')

    for rawLink in soup.select('.article-title'):
        passage = ''
        link = rawLink.attr['href']
        print(link)

grasp_hupu()
