#coding=utf-8
import requests,json,datetime,ConfigParser,re,os

#获取cookies的方法
def Get_Cookie():
    # config = ConfigParser.ConfigParser()
    # file_path = ''.join(re.findall('(.+LcsInterfaceAutomation)', os.getcwd())) + '\Config\config.ini'
    # config.read(file_path)
    # url_login = config.get("LOGIN_URL", "%s"%nick)
    # print url_login

    # 添加登录成功页面的会话
    url_login='http://mc.superboss.cc/mc/readMessage?taobaoId=1119705907'
    header={'Cookie':'cookieid=7ce6f2d86bb20da796c3441079b6da20; gr_user_id=3ab6a459-9924-4fb1-bef2-9ac4fe558c80; _ati=1409220383169; __utmz=250501124.1521620207.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=250501124.|1=versionnum=3=1^3=level=0=1; _ga=GA1.2.602358735.1521620207; h_identify=1c464faddb3da8c7955ee8334780d244; navRedDotRecord=%7B%22%E4%BF%83%E9%94%80%20%20%20%20%22%3Afalse%2C%22%E6%89%93%E5%8D%95%20%20%20%20%22%3Afalse%2C%22%E6%8A%98%E6%89%A3%22%3Afalse%7D; __utma=250501124.602358735.1521620207.1521620207.1523866451.2; identify=78e5ebbe587f13812d842cbecaf37c87; superuseragent=newAgent; truephone=0; isfreeUser=1; jifen=0; picurl=""; shoptype=C; emaileday=0; emailnday=0; emailnnum=0; Hm_lvt_6a46176ff83d6f29a3390a8ae6352d0a=1524462489,1524463760,1524463828,1524464519; activeUrl=null; tjckname=s; super_memSessionId=d0b9d9032af82ad775f6d63e3d1bb59e5a72fbf48e20710af401cb52e422d4f46b33b4be0043a0e2d2ac7bfdf892e24bff0d0173d88a2777fda857e36cefb7cb; visitorId=1119705907; truenick=tb511595_2013; truevisitorId=1119705907; nick=tb511595_2013; versionnum=3; gmtdeadline="2019-05-30 00:00:00"; level=0; trueVersion=3; msgRemain=71281; emailscount=1; wangwang="%E9%80%9A%E7%81%B5%E7%8E%8B,%E5%85%83%E7%9C%9F,%E9%9B%AA%E8%8A%B1,%E5%A4%A9%E6%98%8E,%E6%B7%98%E6%B0%94,%E8%8A%B1%E9%81%93,%E4%B9%94%E5%B7%B4,%E7%B4%AB%E7%BD%97%E5%85%B0,a"; userLevel=V0; msgRemain=71281; Hm_lpvt_6a46176ff83d6f29a3390a8ae6352d0a=1524471165; SERVERID=3ac34f80c391e0c00ccba02b7e3e4513|1524471167|1524465588'}
    session = requests.session()
    session.get(url_login,headers=header)

    # #获取登录成功的cookie
    # cookie=requests.utils.dict_from_cookiejar(session.cookies)
    # super_memSessionId=cookie['super_memSessionId']
    # header={'Cookie': 'super_memSessionId=%s'%super_memSessionId}
    #
    # # 添加短信营销的会话
    # url_crm='http://f.superboss.cc/ProductUsingServlet?kind=108&ftrace=0&gotourl=/customer/customer_query.do'
    # session.get(url_crm,headers=header)
    return session



