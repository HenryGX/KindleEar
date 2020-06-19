#!/usr/bin/env python
# -*- coding:utf-8 -*-
#A GAE web application to aggregate rss and send it to your kindle.
#Visit https://github.com/cdhigh/KindleEar for the latest version
#Contributors:
# rexdf <https://github.com/rexdf>

import gettext

from collections import defaultdict
from apps.BaseHandler import BaseHandler
from apps.dbModels import *
from apps.MyParser import MyParser
import urllib2
from google.appengine.api import mail
import urllib2
import time

class ReptileTask(BaseHandler):
    __url__ = "/reptileTask"
 
    def GET(self):
        reptiles = ReptileSetup.all().filter("name = ", 'admin').get()
        #取得设定URL
        url = reptiles.url
        #获得爬虫设定用户名
        h = history.all().filter("name = ", reptiles.name).get()
        #查看历史count数 如果不存 那么新建
        if not h:
            seths = history(name=reptiles.name,count='0')
            seths.put()
        #取得历史count数
        hs = history.all().filter("name = ", reptiles.name).get()

        #爬虫类实例化 在实例化的函数中解析HTML
        my = MyParser()
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        #取得目标HTML
        htmlStr = response.read() 
        #分析HTML
        my.feed(htmlStr)
        #取得列表 （URL）
        urlList = my.history

        #历史count数比较，发生变化就送信
        if hs.count != str(len(urlList)):
        #     #没有变化邮件送信
        #     self.send_no_mail("ws00381493@gmail.com")
        # else:
            self.send_approved_mail("ws00381493@gmail.com")
            localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
            #送信后记录最近一次送信countshu
            hs.count = str(len(urlList))
            hs.seq = localtime
            hs.put()
            
        

    #邮件发送函数
    def send_approved_mail(self,sender_address):
        # [START send_mail]
        mail.send_mail(sender=sender_address,
                       to="Henry Zhang <ws00381493@gmail.com>",
                       subject="口罩在库更新提示邮件",
                       body="""口罩在库更新""")

                           #邮件发送函数
    def send_no_mail(self,sender_address):
        # [START send_mail]
        mail.send_mail(sender=sender_address,
                       to="Henry Zhang <ws00381493@gmail.com>",
                       subject="没有更新",
                       body="""没有更新""")


