#-*-coding:utf-8-*-
import requests,json,datetime,time
from Common.dianzhang_login import CRM_session
from urllib import urlencode


name=int(time.time()*1000)   #当前时间戳有13位，如果字数限制直接取n个str(now_time)[-n:]
start_time=(datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')  #开始时间
end_time=(datetime.datetime.now()+datetime.timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')    #结束时间
startTime=int(time.mktime(time.strptime(start_time, "%Y-%m-%d %H:%M:%S"))*1000)
endTime=int(time.mktime(time.strptime(end_time, "%Y-%m-%d %H:%M:%S"))*1000)
session=CRM_session('tb511595_2013')

# #新增签到活动
# sign_url='http://dzcrm.superboss.cc/points/activity/create'
# sign_data={"endTime":endTime,"startTime":startTime,"grades":[-1,0,1,2,3,4],"isShow":"true","name":name,"pointSetting":{"0":"1","1":"1","2":"1","3":"1","4":"1","-1":"1"},"ruleDescription":u"活动时间：{0}- {1}\n参与人员：非会员、店铺会员、普通会员、高级会员、VIP会员、至尊VIP\n积分设置：非会员1个积分、店铺会员1个积分、普通会员1个积分、高级会员1个积分、VIP会员1个积分、至尊VIP1个积分\n签到递增奖励：第2天开始，每天额外增加2个积分，连续增加1天后不再增加。".format(start_time,end_time),"type":"sign","increaseReward":{"pointsPerDay":"2","dayToGive":"1"},"skinType":"standard"}
# if json.loads(session.post(sign_url,data=json.dumps(sign_data)).content)['result']=='1':
#     print u'新增签到活动通过'
# search_sign_parmas={'name':name,
#             'stage':'all',
#             'taobaoId':'1119705907',
#             'type':'all',
#             'currentPageNo':'1',
#             'pageSize':'10'}
# search_sign_url='http://crm8.superboss.cc/points/activity/list?'+urlencode(search_sign_parmas)
# search_sign_response=json.loads(session.get(search_sign_url).content)['data']['pager']
# if search_sign_response['totalCount']==1 and search_sign_response['list'][0]['name']==str(name) and search_sign_response['list'][0]['stage']=='notBegin':
#     print u'签到任务列表创建成功'
# else:
#     print u'接口请求成功但签到任务未实际创建'
#
#
# #新增收藏店铺活动
# attention_url='http://dzcrm.superboss.cc/points/activity/create'
# attention_data={"endTime":endTime,"startTime":startTime,"grades":[-1,0,1,2,3,4],"isShow":"true","name":name+10,"pointSetting":{"0":"1","1":"1","2":"1","3":"1","4":"1","-1":"1"},"ruleDescription":u"活动时间：{0}- {1}\n参与人员：非会员、店铺会员、普通会员、高级会员、VIP会员、至尊VIP\n积分设置：非会员1个积分、店铺会员1个积分、普通会员1个积分、高级会员1个积分、VIP会员1个积分、至尊VIP1个积分\n签到递增奖励：第2天开始，每天额外增加2个积分，连续增加1天后不再增加。".format(start_time,end_time),"type":"attention","increaseReward":{"pointsPerDay":"2","dayToGive":"1"},"skinType":"standard"}
# if json.loads(session.post(attention_url,data=json.dumps(attention_data)).content)['result']=='1':
#     print u'新增收藏店铺活动通过'
# search_attention_parmas = {'name': name+10,
#                  'stage': 'all',
#                  'taobaoId': '1119705907',
#                  'type': 'all',
#                  'currentPageNo': '1',
#                  'pageSize': '10'}
# search_attention_url = 'http://crm8.superboss.cc/points/activity/list?' + urlencode(search_attention_parmas)
# search_attention_response = json.loads(session.get(search_attention_url).content)['data']['pager']
# if search_attention_response['totalCount'] == 1 and search_attention_response['list'][0]['name'] == str(name+10) and search_attention_response['list'][0]['stage'] == 'notBegin':
#     print u'收藏店铺任务列表创建成功'
# else:
#     print u'接口请求成功但收藏店铺任务未实际创建'

# #修改消费送积分设置
# consume_url='http://crm8.superboss.cc/points/shop/updateSettings'
# consume_data={"pointPrice":"3","pointsSettingConsume":{"upperLimit":"90"},"sendValueType":"1","pointStatus":1,"gradeSort":{"shopCustomer":"2","normalMember":"3","seniorMember":"7.7","vipMember":"10","extremeMember":"0.1"}}
# if json.loads(session.post(consume_url,data=json.dumps(consume_data)).content)['result']=='1':
#     print u'修改消费送积分设置通过'
#
# #创建兑换积分活动
# exchange_url='http://crm8.superboss.cc/points/gift/create'
# exchange_data={"endTime":endTime,"startTime":startTime,"grades":[0,1,2,3,4],"isShow":"false","name":name+100,"pointSetting":{"0":"1","1":"1","2":"1","3":"1","4":"1"},"ruleDescription":u"兑换时间：2018-06-07 15:55:59 - 2018-06-14 15:55:59\n礼品总数：100件\n每人限兑：4次\n参与人员：店铺会员、普通会员、高级会员、VIP会员、至尊VIP\n积分设置：店铺会员1个积分、普通会员1个积分、高级会员1个积分、VIP会员1个积分、至尊VIP1个积分","type":"coupon","amount":"100","deficiencyNotify":"true","itemId":"1265278854","limited":"4","notifyTelephone":"18667047081"}
# if json.loads(session.post(exchange_url,data=json.dumps(exchange_data)).content)['result']=='1':
#     print u'创建兑换积分活动通过'
# search_exchange_parmas={'name':name+100,
#                       'taobaoId':'1119705907',
#                       'currentPageNo':'1',
#                       'pageSize':'10'}
# search_exchange_url='http://crm8.superboss.cc/points/gift/list?'+ urlencode(search_exchange_parmas)
# search_exchange_response = json.loads(session.get(search_exchange_url).content)['data']['pager']
# if search_exchange_response['totalCount'] == 1 and search_exchange_response['list'][0]['name'] == str(name+100) and search_exchange_response['list'][0]['stage'] == 'notBegin':
#     print u'兑换积分任务列表创建成功'
# else:
#     print u'接口请求成功但兑换积分任务未实际创建'
#
# # #手机主界面设置
# phoneset_url='http://crm8.superboss.cc/points/shop/updateSettings'
# phoneset_data={"color":"#30ae55","shortcuts":[{"img":"","url":"https://crm9.ews.m.jaeapp.com?shopId=1119705907#/sign?id=109"},{"img":"","url":"https://crm9.ews.m.jaeapp.com?shopId=1119705907#/attention?id=113"}],"displaySetting":{"displayCount":"3","showCommodity":"true","showCoupon":"false"}}
# if json.loads(session.post(phoneset_url,data=json.dumps(phoneset_data)).content)['result']=='1':
#     print u'手机主界面设置通过'
#
# #设置积分过期规则
# rule_url='http://crm8.superboss.cc/points/shop/updateSettings'
# rule_data={"pointExpire":"11"}
# if json.loads(session.post(rule_url,data=json.dumps(rule_data)).content)['result']=='1':
#     print u'设置积分过期规则通过'