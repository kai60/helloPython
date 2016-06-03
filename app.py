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
from orm import Model, StringField, IntegerField











def index(request):
    return web.Response(body='<h1>hellp,python</h1>'.encode(encoding='utf-8'),content_type='text/html',charset='uft-8')

@asyncio.coroutine
def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    sever=yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at 127.0.0.1')
    return sever

@asyncio.coroutine
def create_pool(db, password, user, loop, minsize=1, maxsize='10', autocommit=True, charset='utf-8', port='3306',
                host='localhost', **kw):
    logging.info('create database connection')
    global __pool
    __pool=yield from aiomysql.create_pool(host=host, port=port,
                                           user=user, password=password, db=db,
                                           charset=charset, autocommit=autocommit,
                                           maxsize=maxsize, minsize=minsize, loop=loop)









class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()