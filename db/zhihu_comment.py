# coding:utf-8
from db.basic_db import db_session
from db.models import ZhihuComment
from decorators.decorator import db_commit_decorator
from sqlalchemy import text
from sqlalchemy import desc


@db_commit_decorator
def save_comments(comment_list):
    for comment in comment_list:
        r = get_comment_by_id(comment.comment_id)
        if not r:
            save_comment(comment)
    db_session.commit()


@db_commit_decorator
def save_comment(comment):
    db_session.add(comment)
    db_session.commit()


def get_comment_by_id(cid):
    return db_session.query(ZhihuComment).filter(ZhihuComment.comment_id == cid).first()


def get_zhihu_answer_comment_not_crawled():
    return db_session.query(ZhihuComment.comment_id).filter(text('comment_crawled=0')).order_by(desc(ZhihuComment.id)).all()
