# coding:utf-8
import os
import random
from yaml import load

config_path = os.path.join(os.path.dirname(__file__), 'spider.yaml')


with open(config_path, encoding='utf-8') as f:
    cont = f.read()

cf = load(cont)


def get_db_args():
    return {
        "host": "127.0.0.1",
        "port": "3306",
        "user": "root",
        "password": "root",
        "db_name":"zhihu",
        "db_type":"mysql"
    }

def get_broker_and_backend():
    redis_info = cf.get('redis')
    password = redis_info.get('password')
    sentinel_args = redis_info.get('sentinel', '')
    db = redis_info.get('broker', 5)
    if sentinel_args:
        broker_url = ";".join('sentinel://:{}@{}:{}/{}'.format(password, sentinel['host'], sentinel['port'], db) for
                              sentinel in sentinel_args)
        return broker_url
    else:
        host = redis_info.get('host')
        port = redis_info.get('port')
        backend_db = redis_info.get('backend', 6)
        broker_url = 'redis://:{}@{}:{}/{}'.format(password, host, port, db)
        backend_url = 'redis://:{}@{}:{}/{}'.format(password, host, port, backend_db)
        return broker_url, backend_url


def get_db_args():
    return cf.get('db')


def get_redis_args():
    return cf.get('redis')


def get_timeout():
    return cf.get('time_out')

def get_redis_master():
    return cf.get('redis').get('master', '')


def get_code_username():
    return cf.get('yundama_username')


def get_code_password():
    return cf.get('yundama_passwd')


def get_running_mode():
    return cf.get('running_mode')


def get_crawling_mode():
    return cf.get('crawling_mode')


def get_share_host_count():
    return cf.get('share_host_count')


def get_cookie_expire_time():
    return cf.get('cookie_expire_time')


def get_email_args():
    return cf.get('email')
