#!/usr/bin/env python
# encoding: utf-8


"""
@author: Kai
@license: Apache Licence 
@contact: zhufadong@163.com
@site: 
@software: PyCharm
@file: app.py
@time: 16/5/30 17:08
"""

import logging;logging.basicConfig(level=logging.INFO)
import aiohttp,os,json,time,asyncio
from datetime import datetime
from aiohttp import web
import aiomysql
from orm import Model, StringField, BooleanField, FloatField, TextField,create_pool
import uuid

from Models import User, Blog, Comment









def index(request):
    return web.Response(body='<h1>hellp,python</h1>'.encode(encoding='utf-8'),content_type='text/html',charset='uft-8')

@asyncio.coroutine
def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    sever=yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at 127.0.0.1')
    return sever


def test():
    yield from create_pool(user='root', password='root', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()




class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    test()
    loop.run_forever()
