#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2014年01月17日 星期五 10时16分26秒
import os
import sys
import time
import random
import traceback
import json
import types

from parser.ParseService import Iface
from parser.ttypes import Record

class ParserServiceHandler(Iface):
    def __init__(self):
        super(ParserServiceHandler, self).__init__()

    def Parse(self, url, document, cg):
        result = Record("title", "body", "content", "pubsource", "pubtime",
                "author")
        return result

    def Parse2(self, url, document, cg):
        result = Record("title", "body", "content", "pubsource", "pubtime",
                "author")
        return result
