# coding=utf-8
from urllib import parse as url_parse
from db.models import ZhihuData
from db.zhihu_data import insert_zhihu_datas
from http_get_response.basic import get_page
from bs4 import BeautifulSoup
import json

# get search content
# https://www.zhihu.com/r/search?q=https&correction=1&type=content&offset=10
base_url = "https://www.zhihu.com"

def get_search_data(key_word):
    encode_keyword = url_parse.quote(key_word)
    connect_url = "/r/search?q={0}&correction=1&type=content&offset=10".format(encode_keyword)
    page_next = True
    while page_next:
        url = base_url + connect_url
        content = get_page(url)
        page_content = json.loads(content)
        page_next = page_content['paging']['next']
        connect_url = page_content['paging']['next']
        html_list = page_content['htmls']
        if html_list:
            datas = parse_article_list(html_list)
            insert_zhihu_datas(datas)

def parse_article_list(article_list):
    zhihu_data_list = []
    for article in article_list:
        zhihudata = ZhihuData()
        soup = BeautifulSoup(article, 'html.parser')
        zhihudata.zhihu_cont = soup.find(attrs={'class':'js-title-link'}).text
        zhihu_url = soup.find(attrs={'class':'js-title-link'}).get('href')
        zhihudata.zhihu_url = zhihu_url
        zhihudata.zhihu_id = zhihu_url.split('/')[-1]
        zhihudata.create_time = soup.find(attrs={'class':'time text-muted'}).text
        zhihu_data_list.append(zhihudata)
    return zhihu_data_list




