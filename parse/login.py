#encoding:utf-8

import requests,re,time,pdb
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
from http_get_response.header import headers
from db.redis_db import Cookies

#登陆类
class Login:
    def __init__(self):
        self.session = requests.session()

    def getHTMLText(self,url):
        try:
            r = self.session.get(url,timeout=30,headers=headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return None

    def getSoupObj(self,html):
        try:
            soup = BeautifulSoup(html,'html.parser')
            return soup
        except:
            return None

    #是否登录逻辑判断。已登录为True
    def isLogin(self):
        html = self.getHTMLText('https://www.zhihu.com')
        if(str(html).find('<span class="name">') != -1):
            return True
        else:
            return False

    #获取验证码，返回用户输出的验证码
    def getCaptcha(self):
        t = str(int(time.time()*1000))
        captcha_url = 'https://www.zhihu.com/captcha.gif?r={}&type=login'.format(t)
        r = self.session.get(captcha_url,headers=headers)
        with open('captcha.jpg','wb') as f:
            f.write(r.content)
        print('请到程序同级目录下打开captcha.jpg文件，并手动输入验证码')
        captcha = input('请输入验证码: ')
        return captcha

    #获取xsrf
    def getXsrf(self):
        try:
            soup = self.getSoupObj(self.getHTMLText('https://www.zhihu.com'))
            xsrf = soup('input',{'name':'_xsrf'})[0].attrs['value']
            return xsrf
        except:
            return None
    
    def login(self):
        user_name = input('请输入登陆名: ')
        password = input('请输入密码: ')

        #判断登录方式
        if re.match(r'\d{4}-\d{7}|1[34578]\d{9}',user_name):
            print('当前登录方式:手机登陆')
            post_url = 'https://www.zhihu.com/login/phone_num'
            post_data = {'phone_num':user_name,
                         'password':password,
                         '_xsrf':self.getXsrf()
                         }
        else:
            print('当前登录方式:邮箱登陆')
            post_url = 'https://www.zhihu.com/login/email'
            post_data = {'email':user_name,
                         'password':password,
                         '_xsrf':self.getXsrf()
                         }
        try:
            login_page = self.session.post(post_url,headers = headers,data = post_data)
            print(login_page.status)
            print('直接登陆成功!')
        except:
            print('直接登陆失败!')
            post_data['captcha'] = self.getCaptcha()
            login_page = self.session.post(post_url,headers = headers,data = post_data)
            Cookies.store_cookies(user_name, self.session.cookies.get_dict())
            login_code = eval(login_page.text)
            print(login_code['msg'])
