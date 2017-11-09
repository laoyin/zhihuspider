# coding:utf-8
from tasks.workers import app
from db.zhihu_comment import get_zhihu_answer_comment_not_crawled
from parse.parse_answer_comment import get_ajax_comment_data

@app.task(ignore_result=True)
def get_one_answer_comments(comment_id):
    try:
        # comment_id = comment_id[0]
        get_ajax_comment_data(comment_id)
    except Exception as e:
        print(e)


@app.task(ignore_result=True)
def get_answer_comments():
    comment_ids = get_zhihu_answer_comment_not_crawled()
    for comment_id in comment_ids:
        app.send_task('tasks.answer_comment.get_one_answer_comments', args=(comment_id[0]), queue='answer_comment_crawler',
                      routing_key='for_search_info')