# coding:utf-8
import os
import time
import signal
import requests
from .header import headers
from db.redis_db import Urls
from db.redis_db import Cookies
from logger.log import crawler, other
from db.login_info import freeze_account
from utils.email_warning import send_email
# from page_parse.basic import is_403, is_404, is_complete
from decorators.decorator import timeout_decorator, timeout
from config.conf import get_timeout, get_crawl_interal, get_excp_interal, get_max_retries


time_out = get_timeout()
# 暂停时间
interal = get_crawl_interal()
# 尝试请求次数
max_retries = get_max_retries()
# 异常后，暂停时间
excp_interal = get_excp_interal()


def is_banned(url):
    if 'unfreeze' in url or 'accessdeny' in url or 'userblock' in url:
        return True
    return False


@timeout(200)
@timeout_decorator
def get_page(url, need_login=True):
    """
    :param url: url to be crawled
    :param need_login: if the url is need to login, the value is True, else False
    :return: return '' if exception happens or status_code != 200
    """
    crawler.info('the crawling url is {url}'.format(url=url))
    count = 0

    while count < max_retries:
        if need_login:
            name_cookies = Cookies.fetch_cookies()

            if name_cookies is None:
                crawler.warning('no cookies in cookies pool, please find out the reason')
                send_email()
                os.kill(os.getppid(), signal.SIGTERM)
        try:
            if need_login:
                resp = requests.get(url, headers=headers, cookies=name_cookies[1], timeout=time_out, verify=False)
            else:
                resp = requests.get(url, headers=headers, timeout=time_out, verify=False)

            page = resp.text

            if page:
                page = page.encode('utf-8', 'ignore').decode('utf-8')
            else:
                continue
            # slow down to aviod being banned
            time.sleep(interal)

        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError, AttributeError) as e:
            crawler.warning('excepitons happens when crawling {}，specific infos are {}'.format(url, e))
            count += 1
            time.sleep(excp_interal)

        else:
            Urls.store_crawl_url(url, 1)
            return page

    crawler.warning('max tries for {}，check the url in redis db2'.format(url))
    Urls.store_crawl_url(url, 0)
    return ''

__all__ = ['get_page']