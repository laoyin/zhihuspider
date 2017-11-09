# zhihuspider
分布式知乎爬虫，python3，使用celery进行分布式任务分发


使用sqlalchemy做orm框架，
db模块为model、以及相关的存储、创建。

使用redis作为cookies的存储，利用过期时间。
使用redis作为celery的broker，backend。
使用redis作为url任务队列。


2017-11－06完成知乎搜索页面的解析，
知乎搜索，目前可以获取100条查询数据，
问题页面分为两步进行的前端渲染，为了尽可能模仿人的行为，前三条数据，从返回的js中截取数据，再使用ajax获取以后的评论。

init_sql_table.py 创建 db模块下定义的表格。

<!-- 2017-11-07 获取评论的评论。 -->