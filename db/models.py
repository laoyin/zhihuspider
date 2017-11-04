# -*-coding:utf-8 -*-
from db.basic_db import Base
from db.tables import *

class LoginInfo(Base):
    __table__ = login_info

class ZhihuData(Base):
    __table__ = zhihu_data

class KeyWords(Base):
    __table__ = keywords

class KeyWordsZhdata(Base):
    __table__ = keywords_wbdata

class ZhihuComment(Base):
    __table__ = zhihu_comment
