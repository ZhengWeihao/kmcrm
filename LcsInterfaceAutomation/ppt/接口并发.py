#coding=utf-8
import threading
import time,datetime,requests,json
from time import ctime
from Common import get_cookie
from multiprocessing import Process

now_time = datetime.datetime.now().strftime('%Y-%m-%d')
d_time = datetime.datetime.strptime(now_time, '%Y-%m-%d')
time_one = datetime.timedelta(days=5)
end_time=datetime.datetime.strftime(d_time + time_one, '%Y-%m-%d')
# session=get_cookie.Get_Cookie()
numTid='561358925941'                 #商品id

# def cuifu():
#     header={'Cookie':'cookieid=7ce6f2d86bb20da796c3441079b6da20; gr_user_id=3ab6a459-9924-4fb1-bef2-9ac4fe558c80; _ati=1409220383169; __utmz=250501124.1521620207.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=250501124.|1=versionnum=3=1^3=level=0=1; _ga=GA1.2.602358735.1521620207; h_identify=1c464faddb3da8c7955ee8334780d244; navRedDotRecord=%7B%22%E4%BF%83%E9%94%80%20%20%20%20%22%3Afalse%2C%22%E6%89%93%E5%8D%95%20%20%20%20%22%3Afalse%2C%22%E6%8A%98%E6%89%A3%22%3Afalse%7D; __utma=250501124.602358735.1521620207.1521620207.1523866451.2; identify=1c464faddb3da8c7955ee8334780d244; super_memSessionId10034=c8b4b478ad574b1bd3bef0c59c4fdcc0cbbcc2351a2a28cf26cdb25fe6e295f28548fb20609c259092fb1f1c6e8cb5c45c9abe5959049d20a6c4e648f7b875be; superuseragent10034=newAgent; tjckname=s; superuseragent=newAgent; isfreeUser=1; picurl=""; shoptype=C; emaileday=0; emailnday=0; emailnnum=0; Hm_lvt_6a46176ff83d6f29a3390a8ae6352d0a=1524463828,1524464519,1524483846,1524534259; activeUrl=null; numiid=null; versionnum=3; trueVersion=3; super_memSessionId=319063631934a59b7e188ee935acec8bb76e4d64c893e4c2479f0f9a0a6249cc6b33b4be0043a0e2d2ac7bfdf892e24bff0d0173d88a2777fda857e36cefb7cb; visitorId=1119705907; truenick=tb511595_2013; truevisitorId=1119705907; truephone=0; nick=tb511595_2013; jifen=0; gmtdeadline="2019-05-30 00:00:00"; level=0; msgRemain=71281; emailscount=0; userLevel=V0; msgRemain=71281; tj_cookie=334ecd8e719e7cb2e08047f387e1123d; wangwang="%E6%9C%BA%E5%99%A8%E7%8C%AB,%E9%9B%AA%E8%8A%B1,%E6%B7%98%E6%B0%94,%E5%A4%A9%E6%98%8E,%E4%B9%94%E5%B7%B4,%E8%8A%B1%E9%81%93,%E9%80%9A%E7%81%B5%E7%8E%8B,a,%E6%9F%A0%E6%AA%AC%E8%8D%89"; Hm_lpvt_6a46176ff83d6f29a3390a8ae6352d0a=1524563632; SERVERID=3ac34f80c391e0c00ccba02b7e3e4513|1524563662|1524549447'}    #预售催付threading线程
#     data1={
#     '_includeItem':0,
#     'checkBlackList':False,
#     'endPrice':100,
#     'startPrice':1,
#     'endTime':21,
#     'startTime':9,
#     'orderSource':'JHS',
#     'orderFlag':1,
#     'openOrClose':1,
#     'setting':105,
#     'itemUrl':'',
#     'numTid':numTid,
#     'templateContent':'【京东】亲爱的， 还是您最有眼光，看中的是我家XX系列的限量款哦，来晚了就没有了哦，快快支付定金让他彻底属于您哦！@#店铺#u[1119705907](****(买家昵称))(****(买家姓名))(****(订单号)) (****(下单时间))  (****(订单详情)) 退订回TD',
#     'taskName':'林催定金',
#     'checkMemberFilter':'true',
#     'sendCoupon':False,
#     'startDateStr':now_time,
#     'endDateStr':end_time,
#     'receiveInfos':'上海,江苏,浙江',
#     'chooseMobile':'1',
#     'type':78,
#     'newTask':True,
#     'api_name':'saveMarketingSetting'}
#     url='http://crm8.superboss.cc/sms/saveMarketingSetting'
#     print requests.post(url,headers=header,data=data1).content
# for i in range(8):
#     t1 = threading.Thread(target=cuifu)
#     t1.start()
# for i in range(2):
#     url='http://smsquick.superboss.cc/marketing/sendFastSms?filePath=%2Fdata%2Fproject%2Fdianzhang-crm-sms-platform-web%2Fcode%2F%2Ffiles%2FexchangeFiles%2F%E6%A8%A1%E6%9D%BF-2018-02-01-174009%E7%94%A8%E6%88%B7%3Dxxx.txt&fileName=%E6%A8%A1%E6%9D%BF.zip&msg=%E3%80%90%E6%B7%98%E5%AE%9D%E3%80%91%E5%8F%82%E6%95%B0+%E9%80%80%E8%AE%A2%E5%9B%9ETD&phoneSize=1&uploadSize=1'
#     header = {'Cookie': 'cookieid=42168B2A5615C74F1C4831AD28E3D136; _ati=7586380547231; h_identify=1c464faddb3da8c7955ee8334780d244; gr_user_id=6b0c9e05-d492-4739-a8a8-1494fb4516a6; Hm_lvt_6a46176ff83d6f29a3390a8ae6352d0a=1517226848,1517275526,1517361933,1517454144; identify=1c464faddb3da8c7955ee8334780d244; JSESSIONID=315353E2FFE600290110A50672717AE3; super_memSessionId10034=a0b8b22842c091060e832935d53ed8434da95a40e4fd760e48e0a414c51484c0ecac6b2ba5ef19a3d6584e0102d9d3965c9abe5959049d20a6c4e648f7b875be; superuseragent10034=newAgent'}
#     r = json.loads(requests.post(url, headers=header).content)
#     def AdvancePay():
#         r = json.loads(requests.post(url,headers=header).content)
#     threads = []
#     t1 = threading.Thread(target=AdvancePay)
#     threads.append(t1)
#     t1.start()

# def jia(a):
#     while a<40:
#         a=a+1
#         print datetime.datetime.now(),a
# def jian(a):
#     while a>0:
#         a=a-1
#         print datetime.datetime.now(),a
# if __name__ == '__main__':
#     p1=Process(target=jia, args=(20,))
#     p2=Process(target=jian, args=(20,))
#     p1.start()
#     p2.start()

# def fenzu(i):
#     url = 'http://crm4.superboss.cc/blacklist/blacklist_handleBlacklist.do'
#     data = {'type':'1',
#     'blacklist':i}
#     session.post(url,data=data)
# threads = []
# t1 = threading.Thread(target=fenzu,args=((lambda i),for i in range(10),)
# threads.append(t1)
# for thread in threads:
#     thread.start()
#     thread.join()

# if __name__ == '__main__':
#         # print datetime.datetime.now()
#     t1=Process(target=fenzu,args=(i for i in range(10)),)
#     t1.start()
#     t1.join()
# print (echo(i) for i in range(10))
def liqu1():
    url='http://crmad.superboss.cc/activity/addActivityLiBao?appName=dianZhang&taobaoId=385538469'
    header1={'Cookie':'_ati=2167450662154; h_identify=1c464faddb3da8c7955ee8334780d244; identify=44e6e84e463e61eaf4b6f1d1688d783e; UseHasNext=0; nickForStatistics=%E8%80%8D%E6%B5%81%E6%B0%93l; cookieid=92e26b6dfc5b1b7681faafc92fc67ec6; wd_dd_nick=%E8%80%8D%E6%B5%81%E6%B0%93l; pageTypeForStatistics=%E7%9F%AD%E4%BF%A1%E8%90%A5%E9%94%80; tjckname=s; superuseragent=newAgent; isfreeUser=1; shoptype=C; emaileday=0; emailscount=0; Hm_lvt_6a46176ff83d6f29a3390a8ae6352d0a=1527490831,1527558878,1527644876,1527729195; emailnday=0; emailnnum=0; level=0; super_memSessionId=4ff4e4e93e74309ca874a021f38fce7d348e91b73be1ac5f8f54b62de10850526f18b1ac7d04ae04a6d9fca3a96925802d9404200fa48d5888dd8193b204ec38; visitorId=385538469; truenick=china%E4%BA%BA0408; truevisitorId=385538469; truephone=18646190125; nick=china%E4%BA%BA0408; jifen=3700; versionnum=4; gmtdeadline="2018-11-24 00:00:00"; picurl=/07/f1/T1lABeFA0cXXaCwpjX.png; trueVersion=4; msgRemain=478; wangwang="%E9%9B%AA%E8%8A%B1,%E9%80%9A%E7%81%B5%E7%8E%8B,%E6%9C%BA%E5%99%A8%E7%8C%AB,%E8%8A%B1%E9%81%93,%E5%A4%A9%E6%98%8E,%E5%85%83%E7%9C%9F,%E6%9F%A0%E6%AA%AC%E8%8D%89"; userLevel=""; Hm_lpvt_6a46176ff83d6f29a3390a8ae6352d0a=1527733340; SERVERID=a65ddf2e5a877808f5ed78e0b64ea23f|1527733376|1527729292'}
    header2={'Cookie':'_ati=2167450662154; h_identify=1c464faddb3da8c7955ee8334780d244; identify=44e6e84e463e61eaf4b6f1d1688d783e; UseHasNext=0; nickForStatistics=%E8%80%8D%E6%B5%81%E6%B0%93l; cookieid=92e26b6dfc5b1b7681faafc92fc67ec6; wd_dd_nick=%E8%80%8D%E6%B5%81%E6%B0%93l; pageTypeForStatistics=%E7%9F%AD%E4%BF%A1%E8%90%A5%E9%94%80; tjckname=s; superuseragent=newAgent; isfreeUser=1; shoptype=C; emaileday=0; emailscount=0; Hm_lvt_6a46176ff83d6f29a3390a8ae6352d0a=1527490831,1527558878,1527644876,1527729195; emailnday=0; emailnnum=0; super_memSessionId=b4b2dbf48b2c07150f33a3aadac3e8f59c8cc490e8ae98cdc06ffd5186d95a856b33b4be0043a0e2d2ac7bfdf892e24bff0d0173d88a2777fda857e36cefb7cb; visitorId=1119705907; truenick=tb511595_2013; truevisitorId=1119705907; truephone=0; nick=tb511595_2013; jifen=0; versionnum=3; gmtdeadline="2019-05-30 00:00:00"; picurl=""; level=0; trueVersion=3; msgRemain=16998; wangwang="%E6%9F%A0%E6%AA%AC%E8%8D%89,%E9%9B%AA%E8%8A%B1,%E6%9B%BC%E9%99%80%E7%BD%97,%E5%85%83%E7%9C%9F,%E8%8A%B1%E9%81%93,%E6%9C%BA%E5%99%A8%E7%8C%AB,%E5%A4%A9%E6%98%8E"; userLevel=V0; Hm_lpvt_6a46176ff83d6f29a3390a8ae6352d0a=1527730332; SERVERID=a65ddf2e5a877808f5ed78e0b64ea23f|1527730344|1527729292'}
    print requests.get(url,header1).content
def liqu2():
    url='http://crmad.superboss.cc/activity/addActivityLiBao?appName=dianZhang&taobaoId=1119705907'
    header1={'Cookie':'_ati=2167450662154; h_identify=1c464faddb3da8c7955ee8334780d244; identify=44e6e84e463e61eaf4b6f1d1688d783e; UseHasNext=0; tjckname=s; superuseragent=newAgent; isfreeUser=1; emaileday=0; emailscount=0; Hm_lvt_6a46176ff83d6f29a3390a8ae6352d0a=1527470371,1527490831,1527558878,1527644876; super_memSessionId10034=21e167b5a23d8ad7ba138a05557c76ce37f9cbebf281de94eabd73a164dd23ae19cde679d6b9e5723fd7695ba0157af82d9404200fa48d5888dd8193b204ec38; superuseragent10034=newAgent; qianniu_tj=5b6894fbfce62609575e920f05044489; nickForStatistics=%E8%80%8D%E6%B5%81%E6%B0%93l; productTypeForStatistics=%E6%97%BA%E5%BA%97%E4%BA%A4%E6%98%93; cookieid=92e26b6dfc5b1b7681faafc92fc67ec6; wd_dd_nick=%E8%80%8D%E6%B5%81%E6%B0%93l; pageTypeForStatistics=%E7%9F%AD%E4%BF%A1%E8%90%A5%E9%94%80; shoptype=C; truephone=0; jifen=0; super_memSessionId=f05f3ca620f3a085f2a214fa107e0f0c4753f3a6b5d15e88dad264a25c32e0ff3081a0c8355cacb124e716a425462a2eff0d0173d88a2777fda857e36cefb7cb; visitorId=1085048195; truenick=%E8%80%8D%E6%B5%81%E6%B0%93l; truevisitorId=1085048195; nick=%E8%80%8D%E6%B5%81%E6%B0%93l; versionnum=3; gmtdeadline="2018-11-18 00:00:00"; picurl=/b4/5b/TB1MaM4RpXXXXaVXVXXwu0bFXXX.png; level=0; trueVersion=3; msgRemain=26060; emailnday=16; emailnnum=1500; wangwang="%E6%9C%A8%E6%A3%89%E8%8A%B1,%E6%B0%B4%E4%BB%99,%E4%B9%94%E5%B7%B4,%E5%9B%9B%E5%8F%B6%E8%8D%89"; userLevel=""; Hm_lpvt_6a46176ff83d6f29a3390a8ae6352d0a=1527680672; SERVERID=a65ddf2e5a877808f5ed78e0b64ea23f|1527681886|1527680061'}
    header2={'Cookie':'_ati=2167450662154; h_identify=1c464faddb3da8c7955ee8334780d244; identify=44e6e84e463e61eaf4b6f1d1688d783e; UseHasNext=0; nickForStatistics=%E8%80%8D%E6%B5%81%E6%B0%93l; cookieid=92e26b6dfc5b1b7681faafc92fc67ec6; wd_dd_nick=%E8%80%8D%E6%B5%81%E6%B0%93l; pageTypeForStatistics=%E7%9F%AD%E4%BF%A1%E8%90%A5%E9%94%80; tjckname=s; superuseragent=newAgent; isfreeUser=1; shoptype=C; emaileday=0; emailscount=0; Hm_lvt_6a46176ff83d6f29a3390a8ae6352d0a=1527490831,1527558878,1527644876,1527729195; emailnday=0; emailnnum=0; super_memSessionId=b4b2dbf48b2c07150f33a3aadac3e8f59c8cc490e8ae98cdc06ffd5186d95a856b33b4be0043a0e2d2ac7bfdf892e24bff0d0173d88a2777fda857e36cefb7cb; visitorId=1119705907; truenick=tb511595_2013; truevisitorId=1119705907; truephone=0; nick=tb511595_2013; jifen=0; versionnum=3; gmtdeadline="2019-05-30 00:00:00"; picurl=""; level=0; trueVersion=3; msgRemain=16998; wangwang="%E6%9F%A0%E6%AA%AC%E8%8D%89,%E9%9B%AA%E8%8A%B1,%E6%9B%BC%E9%99%80%E7%BD%97,%E5%85%83%E7%9C%9F,%E8%8A%B1%E9%81%93,%E6%9C%BA%E5%99%A8%E7%8C%AB,%E5%A4%A9%E6%98%8E"; userLevel=V0; Hm_lpvt_6a46176ff83d6f29a3390a8ae6352d0a=1527730332; SERVERID=a65ddf2e5a877808f5ed78e0b64ea23f|1527730344|1527729292'}
    print requests.get(url,header2).content
t1 = threading.Thread(target=liqu1)
t2 = threading.Thread(target=liqu2)
threads=[]
threads.append(t1)
threads.append(t2)
for thread in threads:
    thread.start()
    thread.join()


