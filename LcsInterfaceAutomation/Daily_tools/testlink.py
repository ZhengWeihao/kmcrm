#coding=utf-8
import HTMLTestRunner
import datetime
import re,requests,json
from urllib import unquote
import sys
import time
import unittest

#获取erptj的内容审核超级店长列表
url='http://crmtj.superboss.cc/msgCheck/getMessageList'
data={'status': '0', 'sellerNick': '', 'appType': 'dianZhang', 'pageNo': '1', 'api_name': 'msgCheck_getMessageList', 'pageSize': '20'}
header={'Cookie':'ray-authentication=f0aca1515e6246b59ce87ba82fac431f_115.236.53.210;JSESSIONID=DEAFC5AA90D21E575C3447E76A0D9646'}
message_lists=json.loads(requests.post(url,headers=header,data=data).content)['data']['list']
for message_list in message_lists:
    message=message_list['message']
    msgId=message_list['msgId']
    print "%s:%s"%(msgId,unquote(str(message)))

# #根据msgId进行审核，examineType为1是审核通过，examineType为2是审核不通过
# sh_url='http://crmtj.superboss.cc/msgCheck/examineMsgContent'
# sh_data={'msgCount': '1', 'examineType': '2', 'appType': 'dianZhang',
#          'msgId': '810833', 'nick': 'tb511595_2013', 'api_name': 'msgCheck_examineMsgContent',
#         }
# r1=json.loads(requests.post(sh_url,headers=header,data=sh_data).content)['data']['examineResult']
# if r1==1:
#     print '审核通过'
# elif r1==2:
#     print '审核不通过'
# else:
#     print '已被审核'
