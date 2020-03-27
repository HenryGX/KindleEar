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

class ReptileTask(BaseHandler):
    __url__ = "/reptileTask"
 
    def GET(self):
        reptiles = ReptileSetup.all()
        #定时cron调用
        #如何返回结果变动的情况下送信
        #self.send_approved_mail("ws00381493@gmail.com")

        #my = MyParser()
        #my.setUserName(main.session.get('username', ''))
        # url = "https://www.costco.co.jp/search/?text=%E3%83%9E%E3%82%B9%E3%82%AF"
        
        # req = urllib2.Request(url)
        # response = urllib2.urlopen(req)
        # htmlStr = response.read()    
        # my.feed(htmlStr)

        self.send_approved_mail("ws00381493@gmail.com","admin")
        

    #邮件发送函数
    def send_approved_mail(self,sender_address,testName):
        # [START send_mail]
        mail.send_mail(sender=sender_address,
                       to="Henry Zhang <ws00381493@gmail.com>",
                       subject="口罩在库更新提示邮件"+testName,
                       body="""口罩在库更新喽！""")

