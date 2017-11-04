# coding:utf-8
from sqlalchemy import text
from sqlalchemy import desc
from db.basic_db import db_session
from db.models import ZhihuData
from decorators.decorator import db_commit_decorator


@db_commit_decorator
def insert_zhihu_data(zhihu_data):
    db_session.add(zhihu_data)
    db_session.commit()


def get_zh_by_mid(mid):
    return db_session.query(ZhihuData).filter(ZhihuData.zhihu_id == mid).first()


@db_commit_decorator
def insert_zhihu_datas(zhihu_datas):
    for data in zhihu_datas:
        r = get_zh_by_mid(data.zhihu_id)
        if not r:
            db_session.add(data)
    db_session.commit()


@db_commit_decorator
def set_zhihu_comment_crawled(mid):
    zhihu_data = get_zh_by_mid(mid)
    if zhihu_data:
        zhihu_data.comment_crawled = 1
        db_session.commit()


def get_zhihu_comment_not_crawled():
    return db_session.query(ZhihuData.zhihu_id).filter(text('comment_crawled=0')).order_by(desc(ZhihuData.id)).all()


def get_zhihu_repost_not_crawled():
    return db_session.query(ZhihuData.zhihu_id, ZhihuData.uid).filter(text('repost_crawled=0')).all()


@db_commit_decorator
def set_zhihu_repost_crawled(mid):
    zhihu_data = get_zh_by_mid(mid)
    if zhihu_data:
        zhihu_data.repost_crawled = 1
        db_session.commit()