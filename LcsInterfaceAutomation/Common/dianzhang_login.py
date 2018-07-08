#coding=utf-8
import requests,re,json
from Common.read_config import readconfig

header=readconfig('ray-authentication','header')
km_header=readconfig('ray-authentication','km_header')

#通过修改cookie值来获取店长首页的登录地址
def login_url(nick):
    url='http://tj.superboss.cc/item.php?nick={0}'.format(nick)
    jsp_url=requests.get(url,headers=eval(header)).content
    login_url='http://f.superboss.cc/go.jsp?nick=tb511595_2013&mySign{0}&goWhere=pc'.format(re.findall(u'(?<=raycloud_sign)(.*?)(?=<script)',jsp_url)[0])
    return login_url

#通过修改cookie值来获取店长短信营销的登录会话
def CRM_session(nick):
    url='http://tj.superboss.cc/item.php?nick={0}'.format(nick)
    jsp_url=requests.get(url,headers=eval(header)).content
    login_url='http://f.superboss.cc/go.jsp?nick=tb511595_2013&mySign{0}&goWhere=pc'.format(re.findall(u'(?<=raycloud_sign)(.*?)(?=<script)',jsp_url)[0])
    session = requests.session()
    session.get(login_url)
    session.get('http://f.superboss.cc/ProductUsingServlet?kind=108&ftrace=0&gotourl=/customer/customer_query.do')
    return session

#通过修改cookie值来获取快麦的登录会话
def KM_session(nick):
    url='http://kmtj.superboss.cc/base/gotoSellerSystem'
    data={'nick':nick,
         'oType':'crm'}
    km_url=json.loads(requests.post(url, data=data, headers=eval(km_header)).content)['data']['url']
    session=requests.session()
    session.get(km_url)
    return session
