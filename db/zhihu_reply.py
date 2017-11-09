# coding:utf-8
from db.basic_db import db_session
from db.models import ZhihuReply
from decorators.decorator import db_commit_decorator


@db_commit_decorator
def save_replys(reply_list):
    for reply in reply_list:
        r = get_reply_by_id(reply.reply_id)
        if not r:
            save_reply(reply)
    db_session.commit()


@db_commit_decorator
def save_reply(reply):
    db_session.add(reply)
    db_session.commit()

def get_reply_by_id(cid):
    return db_session.query(ZhihuReply).filter(ZhihuReply.reply_id == cid).first()
