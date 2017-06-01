#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# Author: lixingtie
# Email: 260031207@qq.com
# Create Date: 2014-8-11


import json
import datetime
import requests
from bson import ObjectId
from tornado.util import ObjectDict
from framework.web import paging
from framework.mvc.web import RequestHandler
from framework.data.mongo import db, Document, DBRef


class HandlerBase(RequestHandler):
    """
        页面处理器基类
        1. 显示当前用户
        2. 引用全局分页语句
        3. 读取当前用户权限
    """

    def initialize(self):
        pass

    def get_current_user(self):
        token = self.get_secure_cookie("u")
        if not token:
            return None
        c = self.cache.get("BOTS_TOKEN:" + token)
        if c is not None:
            info = json.loads(c)
            return info["user_id"]

    def json(self, obj, content_type="text/json; charset=utf-8", cls=None):
        """
            输出json结果
        """
        self.set_header("Content-Type", content_type)
        self.write(json.dumps(obj, cls=cls).replace("</", "<\\/"))

