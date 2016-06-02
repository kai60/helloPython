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
from sqlalchemy.orm import Model, StringField, IntegerField











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

@asyncio.coroutine
def select(sql,args,size=None):
    logging.info(sql,args)
    global __pool
    with (yield from __pool) as conn:
        cur=yield  from conn.cursor(aiomysql.DictCursor)
        yield  from cur.execute(sql.replace('?','%s'),args or ())
        if size:
            rs=yield  from cur.fetchmany(size)
        else:
            rs=yield  from cur.fetchall()

        yield  from cur.close()
        logging.info('rows returned:%s' % len(rs))
        return rs

@asyncio.coroutine
def execute(sql,args):
    logging.info(sql)
    with (yield  from __pool) as conn:
        try:
            cur=yield  from conn.cursor()
            yield  from cur.execute(sql.replace('?','%s'),args)
            affected=cur.rowcount
            yield  from cur.close()
        except BaseException as e:
             raise e
        return affected


class Field(object):
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)

class StringField(Field):

    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class

class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()