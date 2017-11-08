# coding=utf-8
from db.zhihu_data import get_zhihu_comment_not_crawled
from db.zhihu_comment import save_comments
from db.models import ZhihuComment
from http_get_response.basic import get_page
from bs4 import BeautifulSoup
import json,pdb
# get comment url, http ajax get.
# https://www.zhihu.com/r/answers/3060403/comments
# https://www.zhihu.com/r/answers/3060403/comments?page=2
def get_url(zhihu_data_id):
    url = "https://www.zhihu.com/r/answers/{0}/comments".format(zhihu_data_id)
    return url

base_url = "https://www.zhihu.com/question/{0}"
def get_comment_data():
    zhihu_ids =  get_zhihu_comment_not_crawled()
    for zhihu_id in zhihu_ids[1:]:
        try:
            url  = base_url.format(zhihu_id[0])
            page_content = get_page(url)
            bs_content = BeautifulSoup(page_content)
            jsdata  = bs_content.find(attrs={"id":"data"})
            js_content_json = jsdata["data-state"]
            comment_ids = js_content_json['question']['answers'][id]['ids']
            set_comments_data(comment_ids, js_content_json)
        except Exception as e:
            print(e)
            continue


def set_comments_data(comment_ids, content_json):
    comments = []
    for comment_id in comment_ids:
        zhcomment = ZhihuComment()
        comment_data = content_json['entities']['answers'][comment_id]
        zhcomment.comment_id = comment_id
        zhcomment.comment_cont = comment_data['content']
        print(comment_data['content'])
        zhcomment.zhihu_id = comment_data['id']
        zhcomment.user_id = comment_data['author']['id']
        zhcomment.create_time = comment_data['createdTime']
        comments.append(zhcomment)
    if comments:
        save_comments(comments)
# 解析html页面内容{  }
# begin
# url = question/id 
# content = get_url_result(url)
# # 获取js内容
# data  = BeautifulSoup(content).find(attrs={"id":"data"})
# # 截取js中json
# js_content_json = data["data-state"]
# content_json = json.loads(js_content_json)

# # 获取答案的id
# ids = content_json['question']['answers'][id]['ids']

# # 后去具体答案内容
# for id in ids:
#     content_json['entities']['answers'][id]
    # {'content': '短期利好，英镑贬值，长期利空，英镑升值。<br>感觉欧盟就是个炸弹啊。<br>还有美国都这样子了，还敢加利的话。亏钱我也乐意啊。:)', 'createdTime': 1466477739, 'editableContent': '', 'adminClosedComment': False, 'isSticky': False, 'relationship': {'isNothelp': False, 'voting': 0, 'isAuthorized': False, 'isThanked': False, 'isAuthor': False, 'upvotedFollowees': []}, 'commentCount': 0, 'isCollapsed': False, 'type': 'answer', 'suggestEdit': {'unnormalDetails': {}, 'tip': '', 'url': '', 'status': False, 'reason': '', 'title': ''}, 'commentPermission': 'all', 'annotationAction': [], 'voteupCount': 1, 'isNormal': True, 'canComment': {'status': True, 'reason': ''}, 'reshipmentSettings': 'allowed', 'collapseReason': '', 'excerpt': '短期利好，英镑贬值，长期利空，英镑升值。 感觉欧盟就是个炸弹啊。 还有美国都这样子了，还敢加利的话。亏钱我也乐意啊。:)', 'id': 107036636, 'isCopyable': True, 'rewardInfo': {'rewardMemberCount': 0, 'isRewardable': False, 'canOpenReward': False, 'rewardTotalMoney': 0, 'tagline': ''}, 'updatedTime': 1466477739, 'author': {'gender': 1, 'avatarUrl': 'https://pic1.zhimg.com/50/da8e974dc_hd.jpg', 'isAdvertiser': False, 'avatarUrlTemplate': 'https://pic1.zhimg.com/50/da8e974dc_hd.jpg', 'headline': '', 'type': 'people', 'id': '3b98c670721025670e3ea6fe5c864397', 'followerCount': 7, 'userType': 'people', 'name': '李李', 'badge': [], 'url': 'http://www.zhihu.com/api/v4/people/3b98c670721025670e3ea6fe5c864397', 'urlToken': 'li-li-80-62', 'isOrg': False}, 'collapsedBy': 'nobody', 'url': 'http://www.zhihu.com/api/v4/answers/107036636', 'question': {'questionType': 'normal', 'type': 'question', 'updatedTime': 1464461507, 'url': 'http://www.zhihu.com/api/v4/questions/46866343', 'created': 1464461507, 'id': 46866343, 'title': '英国脱欧对黄金会有影响吗？'}, 'markInfos': [], 'thumbnail': '', 'extras': ''}

# end

# 解析点击页面获取列表内容

# 1:zhihu渲染页面，采用的方式，html渲染3条,
# 2:使用ajax https://www.zhihu.com/api/v4/questions/56620658/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=3&limit=20&sort_by=default


# get 请求:
# include:data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,upvoted_followees;data[*].mark_infos[*].url;data[*].author.follower_count,badge[?(type=best_answerer)].topics
# offset:3
# limit:20
# sort_by:default


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