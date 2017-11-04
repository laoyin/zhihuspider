# coding=utf-8

# get comment url, http ajax get.
# https://www.zhihu.com/r/answers/3060403/comments
# https://www.zhihu.com/r/answers/3060403/comments?page=2
def get_url(zhihu_data_id):
    url = "https://www.zhihu.com/r/answers/{0}/comments".format(zhihu_data_id)
    return url



# Remote Address:118.178.213.186:443
# Request URL:https://www.zhihu.com/r/answers/3060403/comments?page=2
# Request Method:GET
# Status Code:200 OK
# Response Headers
# view source
# Cache-Control:private, no-store, max-age=0, no-cache, must-revalidate, post-check=0, pre-check=0
# Connection:keep-alive
# Content-Encoding:gzip
# Content-Security-Policy:default-src *; img-src * data: blob:; frame-src 'self' *.zhihu.com getpocket.com note.youdao.com read.amazon.cn; script-src 'self' *.zhihu.com unpkg.zhimg.com unicom.zhimg.com *.google-analytics.com res.wx.qq.com 'unsafe-eval'; style-src 'self' *.zhihu.com unicom.zhimg.com 'unsafe-inline'; connect-src * wss:;
# Content-Type:application/json; charset=UTF-8
# Date:Wed, 01 Nov 2017 08:51:07 GMT
# Expires:Fri, 02 Jan 2000 00:00:00 GMT
# Pragma:no-cache
# Server:ZWS
# Set-Cookie:n_c=; Domain=zhihu.com; expires=Tue, 01 Nov 2016 08:51:07 GMT; Path=/
# Transfer-Encoding:chunked
# Vary:Accept-Encoding
# X-Backend-Server:zhihu-web.zhihu-web-other.6c557e55---10.3.109.2:31042[10.3.109.2:31042]
# X-Frame-Options:DENY
# X-Req-ID:69A361E59F98AFB
# X-Req-SSL:proto=TLSv1.2,sni=,cipher=ECDHE-RSA-AES256-GCM-SHA384
# X-Za-Experiment:default:None,ge3:ge3_10,ge2:ge2_1,nweb_sticky_sidebar:sticky,live_review_buy_bar:live_review_buy_bar_2,is_office:false,home_ui2:default,is_show_unicom_free_entry:unicom_free_entry_on,app_store_rate_dialog:close,qa_sticky_sidebar:sticky_sidebar,android_profile_panel:panel_a,live_store:ls_a2_b2_c2_f2,search_hybrid_tabs:without-tabs,answer_related_readings:qa_recommend_with_ads_and_article,asdfadsf:asdfad,new_mobile_column_appheader:new_header,fav_act:default,remix_one_key_play_button:headerButton,mobile_qa_page_proxy_heifetz:m_qa_page_nweb,nweb_write_answer:default,android_pass_through_push:getui,new_more:new,new_buy_bar:livenewbuy3,zcm-lighting:zcm,iOS_newest_version:4.2.0,qrcode_login:qrcode,wechat_share_modal:wechat_share_modal_show
# X-Za-Response-Id:12ea141766da452a
# Request Headers
# view source
# Accept:application/json, text/plain, */*
# Accept-Encoding:gzip, deflate, sdch
# Accept-Language:zh-CN,zh;q=0.8
# Cache-Control:no-cache
# Connection:keep-alive
# Cookie:d_c0="AIDA5r5VLQqPTsxx6wr8SjVZbAiTlZuVzZ0=|1467621068"; _za=25f9a990-c086-402f-91d6-7fa114b8dbaa; _zap=155a64e7-0aa9-4a82-a863-e9cc4cc0972c; _ga=GA1.2.1700925152.1486695548; q_c1=ded886d914124f40b542f2d6a3da53f8|1504850303000|1467621068000; q_c1=ded886d914124f40b542f2d6a3da53f8|1508317693000|1467621068000; aliyungf_tc=AQAAAFLGeEr7kgwA90bteend0/m/pJAG; _xsrf=49fbded86d1dbdb7d90b637c5342b19d; s-t=autocomplete; s-q=https; s-i=2; sid=nbkq2rvg; _xsrf=49fbded86d1dbdb7d90b637c5342b19d; __utma=51854390.1700925152.1486695548.1509503687.1509504170.19; __utmb=51854390.0.10.1509504170; __utmc=51854390; __utmz=51854390.1509503687.18.13.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/22779469; __utmv=51854390.000--|2=registration_date=20160621=1^3=entry_date=20160704=1; l_cap_id="OWUwZWM0OGViOGFkNGU4MThiNWM1NTczZTVlODAzZTE=|1509525854|6b158f6362d021468d8df17edc91462aaaa44ea1"; r_cap_id="MTM3YzVhM2MyOTBjNDUxZThlYTdlYmJiMzczOThkOTE=|1509525854|d1a0ae5c698b9ee05f145e0b03e9146ba7a0d87f"; cap_id="MGFlZGM5YWE0OGNiNDdlYzhkMTRiMDU4YWM2OGYxZmU=|1509525854|f7f13104d6cec3d05fa24e9ff66ef987c43043fd"
# Host:www.zhihu.com
# Pragma:no-cache
# Referer:https://www.zhihu.com/search?type=content&q=https
# User-Agent:Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36
# X-Requested-With:XMLHttpRequest
# X-Xsrftoken:49fbded86d1dbdb7d90b637c5342b19d
# Query String Parameters
# view source
# view URL encoded
# page:2