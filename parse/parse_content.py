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
        zhihudata.zhihu_id = 
        zhihudata.zhihu_cont = soup.find(attrs={'class':'js-title-link'}).text
        zhihudata.comment_num = 
        zhihudata.uid = 
        zhihudata.zhihu_url = soup.find(attrs={'class':'js-title-link'}).get('href')
        zhihudata.create_time = soup.find(attrs={'class':'time text-muted'}).text
        zhihu_data_list.append(zhihudata)
    return zhihu_data_list











'<li class="item clearfix article-item" data-type="Post"><div class="title"><a target="_blank" href="https://zhuanlan.zhihu.com/p/21370073" class="js-title-link">顾亦芯：6.17<em>英国</em>脱欧阴云下原油是涨是跌？今日原油操作建议</a></div><div class="content"><link itemprop="url" href="https://zhuanlan.zhihu.com/p/21370073"><meta itemprop="post-id" content="731850"><meta itemprop="post-url-token" content="21370073"><div class="entry article"><div class="entry-left hidden-phone"><a class="zm-item-vote-count hidden-expanded js-expand js-vote-count" data-bind-votecount>0</a><div class="zm-votebar visible-expanded"><button class="up" title="赞"><i class="icon vote-arrow"></i><span class="label sr-only">赞</span><span class="count">0</span></button></div></div><div class="entry-body"><div class="entry-meta"><strong class="author-line"><a class="author" href="/people/gu-yi-xin-45" data-hovercard="p$t$gu-yi-xin-45">顾亦芯</a></strong></div><div class="entry-content js-collapse-body" data-author-name="顾亦芯" data-entry-url="https://zhuanlan.zhihu.com/p/21370073"><div class="summary hidden-expanded">qq482940100v信gyxx23 【市场重大消息面】 目前比较活跃的依然是美联储<em>加息</em>一事的讨论，虽然说美联储主席耶伦已经明确表示6月不肯能<em>加息</em>，但市场依然不信邪的妄图探讨7月<em>加息</em>可能，因为美联储周三(6月15日)宣布维持指标利率不变，并暗示仍计划在年内<em>升息</em>两…<a class="toggle-expand inline" href="https://zhuanlan.zhihu.com/p/21370073">显示全部</a></div><div class="visible-expanded"><div class="zm-item-vote-info empty" data-votecount="0"><span class="voters"></span> </div><script type="text" class="content">顾亦芯：qq482940100v信gyxx23<br><br><br><br><b>　【市场重大消息面】</b><br><br>　　目前比较活跃的依然是美联储加息一事的讨论，虽然说美联储主席耶伦已经明确表示6月不肯能加息，但市场依然不信邪的妄图探讨7月加息可能，因为美联储周三(6月15日)宣布维持指标利率不变，并暗示仍计划在年内升息两次。这样的兆头并不是好兆头，不过，美联储在声明中下调了今明两年的经济增长预估，同时下调了长期利率预估，暗示其在年底后收紧货币政策的步幅将不再那么积极。<br><br>　　有人称美联储在至少9月份会议之前将几乎肯定不会有机会采取行动，因此7月加息的大门“差不多已经关上”。顾亦芯认为鉴于上次糟糕的非农数据，预计美国劳动力市场增长可能在下半年依然缓慢。紧张的就业市场、企业盈利削弱、政策激励的工资上涨可能会导致经济增长减缓。顾亦芯老师建议投资者密切关注美元、近期的招工形势以及诸如中国因素等全球金融条件，因为这对于理解美联储采取行动的时机将很重要。如果美国就业增长继续放缓，实际通货膨胀率/预期保持适度，国内/国际政治风险搅动市场，那么美联储今年可能难以采取更多正常化步骤。<br><br>　　另一事件就是关于下周举行的英国脱欧公投，市场重心聚焦于此，因为美元的强势反弹以及英国退欧风险加剧重创大宗商品投资情绪，使得油价在昨日盘中重挫逾3%，为连续第六个交易日下跌，创造了1月份以来最长跌势同时触及1个月内低位。此外，虽然美国夏季出行高峰已经到来，但上周原油库存并未出现大幅下降，这令多头情绪受到打压。下周即将举行的英国退欧公投增添了市场的风险厌恶情绪，因此我们可以看到大批投资者锁定获利。顾亦芯认为由于原油多头仓位今年初以来已经达到纪录高位，投资者可能会想要降低风险。<br><p><b> 【原油沥青技术面分析】</b></p><br>　　原油沥青本周连续三个交易日都是这种节奏，主要由于前期的多头较强劲。现在技术面在转成空头，但是由于指标还处于多头通道之中，所以拐头会有所吃力，出现昨日这种反复的走法也就比较常见，主要是蓄势进行下破。现在日图连阴下行，经过昨日的震荡，今日已经将均线系统带动形成死叉，并且失守30日线，日图结构进一步看空。当然这个阶段的空头也只是二浪之中的调整，但这波调整空间不可小瞧。<br><br>　　原油沥青短线图台阶下跌通道保持良好，虽然昨天反抽再次确认了48.68的高点，但是最终没有突破，同时次高点49.30的压制比较强劲，作为下跌通道分界点，反弹49.30下方的修正都是合理范围。短线图跌破47.80支撑位之后，今日具备放量的动能。昨天可以反复，周四的行情一旦起势就是单边。短线只需要用昨日尾盘的高点48.68做止损位继续跟进空单。今日压力位依然在48.0，但今天不一定有昨天的反弹力度。所以顾亦芯建议在欧盘前就要安排好入场位置，否则会踏空点位。<br><b><br>　　【原油沥青操作建议高空为主低多为辅】</b><br><br>　　美原油：<br><br>　　（1）反弹48.0-48.5区间空单进场，严格止损0.5个点，目标看46.0-46.5；<br><br>　　（2）回落44.0-45.0区间多单进场，严格止损0.5个点，目标看47.0-47.5；<br><br>　　宁贵沥青：<br><br>　　（1）回落4420附近做多，目标4470--4500，止损4380.<br><br>　　（2）反弹4500附近做空，止盈4420--4360--4330--4300，止损4540.<br><br><b>【顾亦芯-与君共勉】</b><br><br>　　看过或者注意过亦芯老师昨天晚间接近凌晨时分的策略的朋友应该知道，昨晚的空单思路依旧，并且解套方法都已经给出，聪明的人在趁着那一拨回调早已解决了手中的单子留下后路，迷茫的朋友还在观望，后期行情并没有强劲反弹而是大幅下拉至日内低点，亦芯老师担心你的单子是否扛的住这样的风险，我知道现在很多人不想做空，但是行情如此，事实摆在这里，容不得你不服，不服气的结果就是你的资金受损，这当然是我们大家都不愿意看到的。资本市场就像一把双刃剑，用得好的人成为世人的偶像，用得不好的人小则损失金钱，大则倾家荡产，市场就是这样的残酷没有一点温情可言。趋势已经走出来了，日线连续的六连阴，这么明显的空头行情我不知道各位朋友到底是怎么分析的，也不清楚大家的老师到底是在怎么指导的，在大家都不愿意做空的时候我反其道而行之，并不是没有理由的，事实证明结果很正确，我从来没有要求大家重仓操作，针对没有把握的行情轻仓试探，破位加仓，稳健做单，你看错了这个行情，却说市场欺骗了你。而在这个市场中，你我只要在交易中存活，不是别人的楷模，就是别人的借鉴。听说青蛙只吃动的东西，由此推断：天鹅不动的话青蛙是不会打她主意的，而在单边的时候，你若不逆势空头是不会收割你的金钱的！<br><br><b>一一一一做交易，难在看懂，停在情绪，断在行动，懒在依赖，快在独立，乱在拉人，盈在跟对，苦在单干，巧在借力，亏在自私，错在指责，胜在检讨，差在不改，累在盲目，贵在付出，赔在自大，输在少学，败在放弃，成在坚持。投资其实是一个自我经营的漫长过程。你若愿意跟随,我必倾力奉献！</b></script><a class="time text-muted" href="https://zhuanlan.zhihu.com/p/21370073" data-tooltip="s$t$发布于 2016-06-17" >编辑于 2016-06-17</a></div></div><div class="actions clearfix js-contentActions"><span class="hidden-tablet hidden-desktop"><a href="#" class="action-item votenum-mobile zm-item-vote-count js-openVoteDialog"><span data-bind-votecount>0</span><i class="zg-icon arrow"></i></a></span><a href="#" class="action-item zg-follow js-followButton" data-follow="c:link" data-id="0"><i class="z-icon-follow"></i>关注专栏</a><a href="#" class="action-item js-toggleCommentBox"><i class="z-icon-comment"></i><span class="label">添加评论</span></a><a href="#" class="action-item visible-focusin js-share hidden-phone"><i class="z-icon-share"></i>分享</a><span class="bull visible-focusin hidden-phone">&bull;</span><a href="#" class="action-item visible-focusin js-report hidden-phone">举报</a><span class="hidden-tablet hidden-desktop phone-actions"><a href="#" class="button-text menubutton"><i class="zg-icon zg-icon-ellipsis-mobi"></i><span class="hide-text">更多</span></a><div class="menu goog-menu goog-menu-vertical zh-answer-more-actions" style="display:none"><div class="goog-menuitem js-share">分享</div><div class="goog-menuseparator"></div><div class="goog-menuitem js-report">举报</div></div></span><button class="action-item item-collapse js-collapse"><i class="z-icon-fold"></i>收起</button></div></div></div></div></li>'