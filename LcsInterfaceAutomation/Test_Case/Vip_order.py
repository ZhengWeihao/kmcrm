#-*-coding=utf-8-*-
import requests,json
from Common.dianzhang_login import CRM_session
from time import sleep


url='http://crm8.superboss.cc/sms/saveMarketingSetting'
session=CRM_session('tb511595_2013')
def data(type):
    data1 = {'api_name': 'saveMarketingSetting', 'couponId': '1265278854', 'endPrice': '100', 'startPrice': '1',
             'sendCoupon': 'true', 'checkMemberFilter': 'false', 'checkBlackList': 'true','setting':'60',
             'receiveInfos': u'上海,江苏,浙江,安徽,江西,北京,天津,山西,山东,河北,内蒙古,湖南,湖北,河南,广东,广西,福建,海南,辽宁,吉林,黑龙江,陕西,新疆,甘肃,宁夏,青海,重庆,云南,贵州,西藏,四川,香港,澳门,台湾,海外',
             'alertLevel': '0,1,2,3,4', 'startTime': '9', 'openOrClose': '1', 'endTime': '21', 'type': type,
             'templateContent': u'【淘宝】亲爱的顾客，恭喜您成为本店会员，即日起，购买特定上新宝贝即可享受9折优惠！而且可获得时尚手包一个更多精彩活动期待您的参与 退订回TD'}

    data = {'couponId': '1265278854', 'endPrice': '', 'startPrice': '', 'sendCoupon': 'false', 'checkMemberFilter': 'false',
            'checkBlackList': 'false', 'api_name': 'saveMarketingSetting', 'alertLevel': '', 'startTime': '9',
            'openOrClose': '1', 'endTime': '21', 'type': type,
            'templateContent': u'【淘宝】亲爱的顾客，恭喜您成为本店会员，即日起，购买特定上新宝贝即可享受9折优惠！而且可获得时尚手包一个更多精彩活动期待您的参与 退订回TD',
            'chooseMobile': '0'}
    return data,data1

#会员审计类型type=47,48,49,50
types=['47','48','49','50']
for type in types:
    session.post(url, data=data(type)[0])
#类型type=54,55,56,43
types1=['54','55','56','43']
for type1 in types1:
    session.post(url, data=data(type1)[1])
count=0
while count!=8:
    #获取会员升级的状态
    urge_url='http://crm8.superboss.cc/sms/getMarketingSettingState'
    urge_data={'category':'urge',
               'api_name':'getMarketingSettingState'}
    count1=int(json.loads(session.post(urge_url,data=urge_data).content)['data']['advanced'])+int(json.loads(session.post(urge_url,data=urge_data).content)['data']['common'])+int(json.loads(session.post(urge_url,data=urge_data).content)['data']['supervip'])+int(json.loads(session.post(urge_url,data=urge_data).content)['data']['vip'])

    #获取礼品状态
    care_url='http://crm8.superboss.cc/sms/getAllMemberCareMarketingSettingState'
    care_data={'api_name':'getAllMemberCareMarketingSettingState'}
    count2=int(json.loads(session.post(care_url,data=care_data).content)['data']['hundred'])+int(json.loads(session.post(care_url,data=care_data).content)['data']['moon'])+int(json.loads(session.post(care_url,data=care_data).content)['data']['sleep'])+int(json.loads(session.post(care_url,data=care_data).content)['data']['year'])
    count=count+count1+count2
    if count!=8:
        sleep(60)
else:
    print u'全部审核通过'

