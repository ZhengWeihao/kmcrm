#coding=utf-8
import requests,threading
from urllib import urlencode
url='http://crmad.superboss.cc/activity/addLiBao?'
header1={'Cookie':'identify=1c464faddb3da8c7955ee8334780d244; cookieid=A988749B0A5FF6B181AEEC5D232540DA; tjckname=s; superuseragent=newAgent; isfreeUser=1; emaileday=0; Hm_lvt_6a46176ff83d6f29a3390a8ae6352d0a=1518053212,1518076272; safe_ip=192.168.63.99; safe_identify=%E6%9E%97%E6%98%A5%E7%94%9F; safe_sign=64622d99f2f1a1daf8e9342e631e722e; safe_time=1518076630468; safe_user=%E6%9E%97%E6%98%A5%E7%94%9F; truephone=0; jifen=0; versionnum=3; trueVersion=3; emailscount=0; super_memSessionId=6e00e2e8a9bf2ad006183d03155cb652fec8d0cbf2d2272fb87ef9a4977dfa01bc108af75bad8afad1a4c42e0cb82db32d9404200fa48d5888dd8193b204ec38; visitorId=1119705907; truenick=tb511595_2013; truevisitorId=1119705907; nick=tb511595_2013; gmtdeadline="2018-04-30 00:00:00"; picurl=""; level=0; shoptype=C; msgRemain=3321; emailnday=7; emailnnum=50; wangwang=%25E6%259B%25BC%25E9%2599%2580%25E7%25BD%2597%2C%25E6%25B0%25B4%25E4%25BB%2599%2C%25E7%25B4%25AB%25E7%25BD%2597%25E5%2585%25B0%2C%25E4%25B9%2594%25E5%25B7%25B4%2C%25E9%259B%25AA%25E8%258A%25B1%2C%25E6%259C%25A8%25E6%25A3%2589%25E8%258A%25B1%2Ca%2C%25E6%25B7%2598%25E6%25B0%2594; userLevel=""; Hm_lpvt_6a46176ff83d6f29a3390a8ae6352d0a=1518080752; gr_user_id=41631ae3-7e35-45d9-839e-4e09104767e3; _ati=4662170702836; h_identify=bab9b41cfefdc2528e0630c3f851bfd8'}
header2={'Cookie':'cookieid=27CF5E17DC93D740410A6019E70B97BE; _ati=7197820370026; h_identify=497af41ba79ca99080216cc2f0f55384; identify=06226e5630a35ad1c09d73f6cb64dfd3; tjckname=s; super_memSessionId=d6bee731ef0463c03bc7b48f705d45b6190f895497c78837f948564e5f55929b1a54b9859f4fae83720ca3b8b83b3ce92d9404200fa48d5888dd8193b204ec38; superuseragent=newAgent; truenick=%E5%A4%9A%E6%83%85g%E5%85%AC%E5%AD%90; truevisitorId=2963914609; truephone=13295697392; visitorId=2963914609; isfreeUser=1; nick=%E5%A4%9A%E6%83%85g%E5%85%AC%E5%AD%90; jifen=4150; versionnum=4; gmtdeadline="2018-08-27 00:00:00"; picurl=""; level=1; trueVersion=4; shoptype=C; msgRemain=307; emaileday=0; emailscount=273; emailnday=0; emailnnum=0; wangwang=%25E7%25B4%25AB%25E7%25BD%2597%25E5%2585%25B0%2C%25E6%259B%25BC%25E9%2599%2580%25E7%25BD%2597%2C%25E9%259B%25AA%25E8%258A%25B1%2C%25E6%259C%25A8%25E6%25A3%2589%25E8%258A%25B1%2C%25E4%25B9%2594%25E5%25B7%25B4%2Ca%2C%25E6%25B7%2598%25E6%25B0%2594%2C%25E6%25B0%25B4%25E4%25BB%2599; userLevel=V1; Hm_lvt_6a46176ff83d6f29a3390a8ae6352d0a=1517883312,1517883826,1517984097,1518081117; Hm_lpvt_6a46176ff83d6f29a3390a8ae6352d0a=1518081372'}
parmas1={'area':'浙江省,杭州市,滨江区',
'detailAddress':'滨兴小区西区',
'receiveMobile':'15655511595',
'receiveName':'林春生',
'nick':'tb511595_2013',
'taobaoId':'1119705907',
'type':'2'}
parmas2={'area':'浙江省,杭州市,滨江区',
'detailAddress':'电脑卡六十年代就',
'receiveMobile':'18667047081',
'receiveName':'石江华',
'nick':'多情g公子',
'taobaoId':'2963914609',
'type':'2'}
URL1=url+urlencode(parmas1)
URL2=url+urlencode(parmas2)
def one():
    r1=requests.get(URL1, headers=header1).content
def two():
    r2=requests.get(URL2, headers=header2).content
threads = []
t1 = threading.Thread(target=one)
t2 = threading.Thread(target=two)
threads.append(t1)
threads.append(t2)
for t in threads:
    t.start()
