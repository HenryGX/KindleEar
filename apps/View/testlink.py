#!/usr/bin/env python
# -*- coding:utf-8 -*-
#A GAE web application to aggregate rss and send it to your kindle.
#Visit https://github.com/cdhigh/KindleEar for the latest version
import datetime, urlparse
try:
    import json
except ImportError:
    import simplejson as json
from apps.utils import etagged
import web
from apps.BaseHandler import BaseHandler
from apps.dbModels import *
from lib.urlopener import URLOpener
from google.appengine.api import urlfetch

#网友共享的订阅源数据
class testLink(BaseHandler):
    __url__ = "/testlink"

    @etagged()
    def GET(self,tips=None):
        user = self.getcurrentuser()
        reptile = self.getReptile()
        return self.render('testlink.html', "testlink", current='testlink', user=user, reptile=reptile, tips=tips, res=None)

    #分享了一个订阅源
    def POST(self):
        reptile = self.getReptile()
        webInput = web.input()
        email = webInput.get('email')
        corn_time = webInput.get('corn_time')
        url = webInput.get('url')
        if not email:
            tips = _("请输入邮箱地址!")
        else:
            reptile.email = email
            reptile.corn_time = corn_time
            reptile.url = url
            reptile.put()
            tips = _("Settings Saved!")

        return self.GET(tips)