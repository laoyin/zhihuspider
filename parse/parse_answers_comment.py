# coding=utf-8
from db.zhihu_comment import get_zhihu_answer_comment_not_crawled
from db.models import ZhihuReply
from db.zhihu_reply import save_replys
from http_get_response.basic import get_page
from bs4 import BeautifulSoup
import json,pdb
# get comment url, http ajax get.
# https://www.zhihu.com/r/answers/3060403/comments
# https://www.zhihu.com/r/answers/3060403/comments?page=2
# def get_ajax_url(answer_id):
#     url = "https://www.zhihu.com/r/answers/{0}/comments?include=data%5B*%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author&order=normal&limit=20&offset=0&status=open".format(answer_id)
#     return url

def get_ajax_url(answer_id):
    url = "https://www.zhihu.com/r/answers/{0}/comments".format(answer_id)
    return url

def get_answer_comments():
    comment_ids = get_zhihu_answer_comment_not_crawled()
    for comment_id in comment_ids:
        try:
            comment_id = comment_id[0]
            get_ajax_comment_data(comment_id)
        except Exception as e:
            print(e)
            continue

def get_ajax_comment_data(comment_id):
    pdb.set_trace()
    comment_id = '75533120'
    limit = 20
    offset = 0
    # search_ajax_url = get_ajax_url(comment_id)
    search_ajax_url = "https://www.zhihu.com/api/v4/answers/75533120/comments?include=data%5B*%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author&order=normal&limit=20&offset=0&status=open"
    is_end = False
    pdb.set_trace()
    while (not is_end):
        try:
            page_content = get_page(search_ajax_url)
            print(page_content)
            json_content = json.loads(page_content)
            is_end = json_content['paging']['is_end']
            search_ajax_url = json_content['paging']['next']
            set_ajax_answer_comments_data(comment_id, json_content['data'])
        except Exception as e:
            print(e)
            is_end = True

def set_ajax_answer_comments_data(comment_id, datas):
    replys = []
    for data in datas:
        reply = ZhihuReply()
        reply.reply_id = data['id']
        reply.reply_cont = data['content']
        reply.create_time = data['created_time']
        reply.comment_id = comment_id
        reply.user_id = data["author"]['member']['id']
        replys.append(reply)
    if replys:
        save_replys(replys)