# -*-coding:utf-8 -*-
from sqlalchemy import Table, Column, INTEGER, String, Text
from db.basic_db import metadata

# login table
login_info = Table("login_info", metadata,
                   Column("id", INTEGER, primary_key=True, autoincrement=True),
                   Column("name", String(100), unique=True),
                   Column("password", String(200)),
                   Column("enable", INTEGER, default=1, server_default='1'),
                   )


zhihu_data = Table("zhihu_data", metadata,
                   Column("id", INTEGER, primary_key=True, autoincrement=True),
                   Column("zhihu_id", String(200), unique=True),
                   Column("zhihu_cont", Text),
                   Column("zhihu_img", String(1000)),
                   Column("zhihu_video", String(1000)),
                   Column("repost_num", INTEGER, default=0, server_default='0'),
                   Column("comment_num", INTEGER, default=0, server_default='0'),
                   Column("praise_num", INTEGER, default=0, server_default='0'),
                   Column("uid", String(20)),
                   Column("is_origin", INTEGER, default=1, server_default='1'),
                   Column("device", String(200), default='', server_default=''),
                   Column("zhihu_url", String(300)),
                   Column("create_time", String(200)),
                   Column("comment_crawled", INTEGER, default=0, server_default='0'),
                   Column("repost_crawled", INTEGER, default=0, server_default='0'),
                )

# search keywords table
keywords = Table('keywords', metadata,
                 Column("id", INTEGER, primary_key=True, autoincrement=True),
                 Column("keyword", String(200), unique=True),
                 Column("enable", INTEGER, default=1, server_default='1'),
                 )

# keywords and weibodata relationship
keywords_wbdata = Table('keywords_wbdata', metadata,
                        Column("id", INTEGER, primary_key=True, autoincrement=True),
                        Column("keyword_id", INTEGER),
                        Column("zh_id", String(200)),
                        )

# comment table
zhihu_comment = Table('zhihu_comment', metadata,
                      Column("id", INTEGER, primary_key=True, autoincrement=True),
                      Column("comment_id", String(50)),
                      Column("comment_cont", Text),
                      Column("zhihu_id", String(200)),
                      Column("user_id", String(20)),
                      Column("create_time", String(200)),
                      )