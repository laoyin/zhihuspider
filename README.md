# zhihuspider
分布式知乎爬虫，python3，使用celery进行分布式任务分发


使用sqlalchemy做orm框架，
db模块为model、以及相关的存储、创建。

使用redis作为cookies的存储，利用过期时间。
使用redis作为celery的broker，backend。
使用redis作为url任务队列。


2017-11－06完成知乎搜索页面的解析，
问题页面答案分为两步进行的前端渲染，为了尽可能模仿人的行为，前三条数据，从返回的js中截取数据，再模拟ajax获取以后的评论。

2017-11-10完成答案的评论, table 定义为reply, 深度抓取对用户答案的评论.




init_sql_table.py 创建db下定义的表格。
crawl_answer.py 抓取ZhihuData下 comment_crawled为0的问题答案
crawl_reply.py 抓取答案的评论
<!-- 2017-11-07 获取评论的评论。 -->