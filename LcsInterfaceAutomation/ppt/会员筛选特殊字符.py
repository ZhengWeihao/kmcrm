#coding=utf-8
import time,datetime,requests,json,sys
from time import ctime,sleep
from Common import get_cookie
from urllib import urlencode

reload(sys)
sys.setdefaultencoding('utf-8')

header={'Cookie':'cookieid=7ce6f2d86bb20da796c3441079b6da20; gr_user_id=3ab6a459-9924-4fb1-bef2-9ac4fe558c80; _ati=1409220383169; __utmz=250501124.1521620207.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=250501124.|1=versionnum=3=1^3=level=0=1; _ga=GA1.2.602358735.1521620207; h_identify=1c464faddb3da8c7955ee8334780d244; navRedDotRecord=%7B%22%E4%BF%83%E9%94%80%20%20%20%20%22%3Afalse%2C%22%E6%89%93%E5%8D%95%20%20%20%20%22%3Afalse%2C%22%E6%8A%98%E6%89%A3%22%3Afalse%7D; __utma=250501124.602358735.1521620207.1521620207.1523866451.2; identify=1c464faddb3da8c7955ee8334780d244; super_memSessionId10034=c8b4b478ad574b1bd3bef0c59c4fdcc0cbbcc2351a2a28cf26cdb25fe6e295f28548fb20609c259092fb1f1c6e8cb5c45c9abe5959049d20a6c4e648f7b875be; superuseragent10034=newAgent; tjckname=s; superuseragent=newAgent; isfreeUser=1; picurl=""; shoptype=C; emaileday=0; emailnday=0; emailnnum=0; Hm_lvt_6a46176ff83d6f29a3390a8ae6352d0a=1524463828,1524464519,1524483846,1524534259; activeUrl=null; numiid=null; versionnum=3; trueVersion=3; super_memSessionId=319063631934a59b7e188ee935acec8bb76e4d64c893e4c2479f0f9a0a6249cc6b33b4be0043a0e2d2ac7bfdf892e24bff0d0173d88a2777fda857e36cefb7cb; visitorId=1119705907; truenick=tb511595_2013; truevisitorId=1119705907; truephone=0; nick=tb511595_2013; jifen=0; gmtdeadline="2019-05-30 00:00:00"; level=0; msgRemain=71281; emailscount=0; userLevel=V0; msgRemain=71281; tj_cookie=334ecd8e719e7cb2e08047f387e1123d; wangwang="%E6%9C%BA%E5%99%A8%E7%8C%AB,%E9%9B%AA%E8%8A%B1,%E6%B7%98%E6%B0%94,%E5%A4%A9%E6%98%8E,%E4%B9%94%E5%B7%B4,%E8%8A%B1%E9%81%93,%E9%80%9A%E7%81%B5%E7%8E%8B,a,%E6%9F%A0%E6%AA%AC%E8%8D%89"; Hm_lpvt_6a46176ff83d6f29a3390a8ae6352d0a=1524563632; SERVERID=3ac34f80c391e0c00ccba02b7e3e4513|1524563662|1524549447'}
select_url='http://crm8.superboss.cc/marketing/queryMember?'
parmas={'buyerNick':'流氓大人55:',
        'limitDay':'1',
        'specifycommodity':'0',
        'returnValue':'true',
        'pageNo':'1',
        'pageSize':'10'
        }
Select_url=select_url+urlencode(parmas)
data=json.loads(requests.get(Select_url,headers=header).content)
try:
    assert data['result']==u'1'
except AssertionError:
    print '会员筛选发送查询失败',data
