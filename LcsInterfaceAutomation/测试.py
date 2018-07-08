#coding=utf-8
import requests,json,datetime
from urllib import urlencode

#注册
# url='http://smsquick.superboss.cc/user/register?'
# parmas={'inviterId':'12312',
#       'password':'123456',
#         'telephone':'15157192380',
#         'username':'大头儿子1'}
# print url+urlencode(parmas)
# print requests.get(url+urlencode(parmas)).content


# url='http://smsquick.superboss.cc/user/login'
# data={'password':'e10adc3949ba59abbe56e057f20f883e',
#       'telephone':'18667047081'}
# session=requests.session()
# session.post(url,data=data)
# data_url='http://smsquick.superboss.cc'

# #分页展示被邀请人信息
# parmas1={'pageNo':1,
#          'pageSize':10}
# print session.get(data_url+'/user/invitShow'+'?'+urlencode(parmas1)).content

# #回显收款账号信息
# print session.get(data_url+'/user/viewAccountInfo').content

# #奖励领取记录查询
# parmas2={'pageNo':1,
#          'pageSize':10}
# print session.get(data_url+'/user/rewardReceiveRecord'+'?'+urlencode(parmas2)).content

# #生成邀请链接
# print session.get('http://smsquick.superboss.cc/user/generateInviteShortChain').content

# #设置收款账号信息
# parmas3={'aliPayAccount':'123',
#          'aliPayName':'123'}
# print session.get(data_url+'/user/setUpAccountInfo'+'?'+urlencode(parmas3)).content

# #邀请人相关信息展示
# print session.get(data_url+'/user/invitHeaderInfo').content

# #领取推荐奖励
# parmas4={'level':1}
# print session.get(data_url+'/user/receiveRecommendReward'+'?'+urlencode(parmas4)).content


url='http://tj.superboss.cc/item.php?nick=好奇害死猫吗'
header={'Cookie': 'ray-authentication=bc57734da23e44b59847dc79fc785976_115.236.53.210'}
r=requests.get(url,headers=header).content
print r









