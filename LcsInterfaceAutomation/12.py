#coding=utf-8
import requests,json,xlrd,xlutils,xlwt,sys,datetime
from xlutils.copy import copy
from urllib import urlencode,unquote
from Common import get_cookie
from time import sleep
from Common import dianzhang_login
reload(sys)
sys.setdefaultencoding('utf-8')

session=dianzhang_login.CRM_session('tb511595_2013')
url='http://crm8.superboss.cc/member/memberImport'
files = {'file': open(r'D:\LcsInterfaceAutomation\TestFiles\ExportOrderList201712191109.csv', 'rb')}
print session.post(url,files=files).content,files

# parmas={
# 'limitDay':'1',
# 'specifycommodity':'0',
# 'returnValue':'true',
# 'pageNo':'1',
# 'pageSize':'1000000'
# }
# session=get_cookie.Get_Cookie('2014最爱夜蒲')[0]
# data_url='http://crm8.superboss.cc/marketing/queryMember'
# url=data_url+'?'+urlencode(parmas)
# print session.get(url).content

# print session.get(url).content
# a=u'【淘宝】该来的都会来，该走的都会走，别抗拒，别不舍，别担心！就现在，双十二禾少杀已经开启啦！店铺链接xxxu[1119705907]u[1119705907]u[1119705907]u[1119705907] 退订回TD'
# c=0
# for i in list(a.decode('utf-8')):
#     c=c+1
# print c
# session=get_cookie.Get_Cookie('tb511595_2013')[0]
# data={
#     'buyerNick':'华仔减油啊啊',
#     'blacklistMarketing':'1',
#     'specifycommodity':'0',
#     'grade':'1,2,3,4',
#     'limitDay':'-1',
#     'api_name':'queryMember',
#     'msg':'【淘宝】123 退订回TD',
#     'mrnd':'0.4730630791490835',
#     'sendCount':'1',
#     'couponId':'1053633031'
#     }
# url='http://crm8.superboss.cc/coupon/sendCouponAndMsg'
# print session.post(url,data=data).content

#会员筛选发送时间接口测试
# data={
# 'buyerNick':'流氓大人55',
# 'limitDay':'-1',
# 'specifycommodity':'0',
# 'realCount':'1',
# 'sendTime':'2018-01-14 23:18:52',
# 'msg':'【超级店长】123 退订回TD',
# 'api_name':'sendMsg'
# }
# session=get_cookie.Get_Cookie('tb511595_2013')[0]
# url='http://dzcrm.superboss.cc/marketing/sendMsg'
# r=session.post(url,data=data).content
# print r

# #指定号码时间接口测试
# data={
#     'isTest':'false',
# 'sendTime':'2018-01-15 22:45:48',
# 'phones':'15655511595',
# 'msg':'【超级店长】12312 退订回TD',
# 'api_name':'sendManualMsg'
# }
# session=get_cookie.Get_Cookie('tb511595_2013')[0]
# url='http://dzcrm.superboss.cc/marketing/sendManualMsg'
# r=session.post(url,data=data).content
# print r

# url1='http://crmad.superboss.cc/test/setLiBaoNum?type=kaiNianDaJi2018&appName=dianzhang&num=0'
# url2='http://crmad.superboss.cc/test/setLiBaoNum?type=daXie2017&appName=dianzhang&num=0'
# r=requests.get(url2).content
# print r

# url='https://wdst2.superboss.cc/wdcrm/sms/set_sms_setting_detail'
# header={'cookie':'_ati=762125070596; _uab_collina=152541481965084102957696; cookieid=a988749b0a5ff6b181aeec5d232540da; navRedDotRecord=%7B%22%E4%BA%A4%E6%98%93%20%20%20%20%22%3Afalse%7D; qnevent=; super_memSessionId=2c5cfcb9a8175cc6e623961a8c32a5c03a36d4c9247f7a9943fc5a67980105e06b33b4be0043a0e2d2ac7bfdf892e24bff0d0173d88a2777fda857e36cefb7cb; superuseragent=newAgent; truenick=tb511595_2013; truevisitorId=1119705907; truephone=0; ztcbl=0; visitorId=1119705907; isfreeUser=1; nick=tb511595_2013; jifen=0; versionnum=3; gmtdeadline="2019-05-30 00:00:00"; picurl=""; level=0; trueVersion=3; shoptype=C; msgRemain=82183; emaileday=1; emailscount=0; emailnday=0; emailnnum=0; wangwang="%E6%9F%A0%E6%AA%AC%E8%8D%89,%E5%85%83%E7%9C%9F,%E8%8A%B1%E9%81%93,%E4%B9%94%E5%B7%B4,%E6%9C%BA%E5%99%A8%E7%8C%AB,a,%E5%A4%A9%E6%98%8E"; Hm_lvt_6a46176ff83d6f29a3390a8ae6352d0a=1525831665,1525859004,1525918124,1526017156; Hm_lpvt_6a46176ff83d6f29a3390a8ae6352d0a=1526017156; memSessionId=55968ef457b6553fadbc40a29b88fa3de88ceab1e54289d1befeb94f99e231f60a0c14322d951721392b987f866f7f5d66e5d581283fb34c3cf9803052a8fd9f5462cd2833f761b094f19580f646268536fb6d157b8d75890e6b4b29a28d2ae3; _umdata=E2AE90FA4E0E42DE8EA7E9747C87C63FA99206F70D5400A682E5A539D3F83B17579DF048C172B9DACD43AD3E795C914C1072A94A33D0CF000450B71F42B2FB0A; nickForStatistics=tb511595_2013; UseHasNext=0; wd_dd_nick=tb511595_2013; qianniu_tj=9b134feec9bb1ae6df16ebfc87a16f6c; productTypeForStatistics=%E6%97%BA%E5%BA%97%E4%BA%A4%E6%98%93; productTypeForStatistics=%E6%97%BA%E5%BA%97%E4%BA%A4%E6%98%93; pageTypeForStatistics=%E7%9F%AD%E4%BF%A1%E8%90%A5%E9%94%80; JSESSIONID=B85B0703981985FF8E30A5485D3EB27B'}
# data={'user_id':'1119705907',
# 'turn_on':'true',
# 'category':'CARE_HAVE_PAY',
# 'sms_template':'【旺店交易】感谢您的信任，我们将全心全意为您服务！店铺新品东京富士山大阪京都一日游产品，最高优惠40元！数量有限。',
# 'is_member_filter':'false',
# 'api_name':'set_sms_setting_detail'}
# r=requests.post(url,headers=header,data=data).content
# print r

# header={'Cookie':'h_identify=1c464faddb3da8c7955ee8334780d244; _ati=8595930628229; UseHasNext=0; identify=78e5ebbe587f13812d842cbecaf37c87; nickForStatistics=%E7%88%B1%E4%B8%8A%E6%9E%AB; cookieid=23adc68feb36eb5615a57c4b107edd57; wd_dd_nick=%E7%88%B1%E4%B8%8A%E6%9E%AB; pageTypeForStatistics=%E7%9F%AD%E4%BF%A1%E8%90%A5%E9%94%80; super_memSessionId=3e9817ba501b65d7545bba629bbb7c275931bbd62c37a5b5990ed0c611399a5b23f47870aae85f302873fe83cae252333283f0b112ee5215de7c6841870d8702; superuseragent=newAgent; visitorId=1119705907; truenick=tb511595_2013; truevisitorId=1119705907; truephone=0; isfreeUser=1; nick=tb511595_2013; jifen=0; versionnum=3; gmtdeadline="2019-05-30 00:00:00"; picurl=""; level=0; trueVersion=3; shoptype=C; msgRemain=128933; emaileday=0; emailscount=0; emailnday=0; emailnnum=0; wangwang="%E9%9B%AA%E8%8A%B1,a,%E7%B4%AB%E7%BD%97%E5%85%B0,%E4%B9%94%E5%B7%B4,%E5%A4%A9%E6%98%8E,%E6%9C%BA%E5%99%A8%E7%8C%AB,%E6%9F%A0%E6%AA%AC%E8%8D%89,%E8%8A%B1%E9%81%93"; Hm_lvt_6a46176ff83d6f29a3390a8ae6352d0a=1525914915,1525953895,1526003784,1526112860; userLevel=V0; SERVERID=bdd4a9deb072e21a25f2f633144cf911|1526112898|1526112874; Hm_lpvt_6a46176ff83d6f29a3390a8ae6352d0a=1526112898'}
# a='groupType=manual&groupName=600111006'
# data=dict([item.split('=') for item in a.split('&')])
# r=requests.post('http://crm4.superboss.cc/memberGroup/memberGroup_saveNewGroup.do',headers=header,data=data).content
# print r

# data={'user_id':'false',
# 'category':'SEND_URGE_PAY',
# 'api_name':'get_sms_setting_detail'}
# r=session.post('https://wdst2.superboss.cc/wdcrm/sms/get_sms_setting_detail',data=data).co

# r='ie=utf-8&mod=1&isbd=1&isid=fb8862f400005d57&ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python%20dict%E5%87%BD%E6%95%B0&oq=python%2520dict%25E5%2587%25BD%25E6%2595%25B0&rsv_pq=fb8862f400005d57&rsv_t=9004sBw7%2Bbnwc3OXCLYCjCF4C6Ijk1eDHNWuP0qcArax%2BXi3yGrOCtnE654&rqlang=cn&rsv_enter=0&bs=python%20dict%E5%87%BD%E6%95%B0&rsv_sid=undefined&_ss=1&clist=&hsug=&f4s=1&csor=13&_cr1=29247Names?ie=utf-8&mod=1&isbd=1&isid=fb8862f400005d57&ie=u…fined&_ss=1&clist=&hsug=&f4s=1&csor=13&_cr1=29247s?ie=utf-8&csq=1&pstg=20&mod=2&isbd=1&cqid=ebbaafb…38.1.143.19.7.680.18&isnop=0&rsv_stat=-2&rsv_bp=1'
# print [item.split('=') for item in r.split('&')]

# a='ie=utf-8&mod=1&isbd=1&isid=fb8862f400005d57&ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python%20dict%E5%87%BD%E6%95%B0&oq=python%2520dict%25E5%2587%25BD%25E6%2595%25B0&rsv_pq=fb8862f400005d57&rsv_t=9004sBw7%2Bbnwc3OXCLYCjCF4C6Ijk1eDHNWuP0qcArax%2BXi3yGrOCtnE654&rqlang=cn&rsv_enter=0&bs=python%20dict%E5%87%BD%E6%95%B0&rsv_sid=undefined&_ss=1&clist=&hsug=&f4s=1&csor=13&_cr1=29247'
# print dict([item.split('=') for item in a.split('&')]

#url='http://safe.raycloud.com/libs/runtime/permission/requestAuthCode'
# header={'Cookie':'corpId=ding789c4e68684e3f26'}
url='http://safe.raycloud.com/qrcode/dd_user.jsp'
header={'Cookie':'JSESSIONID=DD05A7E49D9CB7FC8ED4AC2D3786C9A4'}
session = requests.session()
session.get(url,headers=header)
cookie=requests.utils.dict_from_cookiejar(session.cookies)
