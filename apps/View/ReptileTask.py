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
from apps.utils import local_time
from books import BookClass

from google.appengine.api import app_identity
from google.appengine.api import mail
import webapp2

from google.appengine.api import taskqueue

class ReptileTask(webapp2.RequestHandler):
    __url__ = "/reptileTask"
 
#     def GET(self):
#         reptiles = ReptileSetup.all()
#         #定时cron调用
#         sentcnt = 0


    def GET(self):
        reptiles = ReptileSetup.all()
        #定时cron调用
        sentcnt = 0
        fromMail = "ws00381493@gmail.com"
        toMail = "ws00381493@gmail.com"
        taskqueue.add(url='/worker', queue_name="deliverqueue1", method='GET',
                params=param, target="worker")



# def send_approved_mail(sender_address):
#     # [START send_mail]
#     mail.send_mail(sender=sender_address,
#                    to="Henry Zhang <ws00381493@gmail.com>",
#                    subject="Your account has been approved",
#                    body="aaa")
#     # [END send_mail]


# class ReptileTask(BaseHandler):
#     __url__ = "/reptileTask"
#     def get(self):
#         send_approved_mail("ws00381493@gmail.com")
        
#         return "Put <strong>3</strong> books to queue!"

