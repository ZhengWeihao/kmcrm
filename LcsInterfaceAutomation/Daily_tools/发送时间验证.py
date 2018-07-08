#-*-coding=utf-8-*-
import requests,json,re,sys
from urllib import urlencode

reload(sys)
sys.setdefaultencoding('utf-8')
#获取店长短信营销session
url='http://f.superboss.cc/go.jsp?nick=tb511595_2013&mySign=19e8ab3ff3519a6845a179c52d283ff6&goWhere=pc'
session1=requests.session()
session1.get(url)
session1.get('http://f.superboss.cc/ProductUsingServlet?kind=108&ftrace=0&gotourl=/customer/customer_query.do')
# 智能营销
# znyx_url = 'http://crm8.superboss.cc/marketing/saveMarketingActivityStrong'
# znyx_data = {"marketingStrongStr": json.dumps({"details": [{"content": u"【超级店长】亲爱的，店铺名周年遇上618，感谢有你相伴，好评荭包大派送，进店领取！ 退订回TD", "memTitle": u"近半年店铺会员", "id": "10010","type": "0", "runEnd": "", "runPoint": "", "runStart": "", "runType": "1", "testMobile": "", "jobName": u"即时","extra": "{\"sceneType\":\"\",\"sceneCrowdVal\":\"\",\"screenType\":2}","sendTime": '2018-07-05 02:44:23'}],"conditionVOs": [{"blacklistMarketing": "", "buyerNick": "", "endBuyCount": "","endBuyFee": "", "endDate": "2018-06-04", "grade": "","groupIndexStr": "", "limitDay": "1", "receiverState": "","startBuyCount": "6", "startBuyFee": "","startDate": "2017-12-06", "setCf": "", "specifycommodity": 0,"numIid": ""}], "jobName": "dssss", "templateName": u"标准版","isTemplate": "false"}),
#              "api_name": "saveMarketingActivityStrong"}
# print u"店长智能营销：%s" % session1.post(znyx_url,data=znyx_data).content




# ------订单筛选、会员升级、优惠券无定时发送------
def send_time(send_time):
      #会员筛选发送
      hysx_url='http://crm8.superboss.cc/marketing/sendMsg'
      hysx_data={'limitDay':'-1',
        # 'buyerNick': u'枫中的思念',
        'receiverName':u'徐俊华',
        'specifycommodity':'0',
        'realCount':'1',
        'sendTime':send_time,
        'msg':u'【多情g公子】亲爱的，拍下的交易剩下时间不多啦，即将要关闭了哦，喜欢的话抓紧时间付款，祝您购物愉快。 退订回TD',
        'api_name':'sendMsg'}
      print u"店长会员筛选发送：%s" %session1.post(hysx_url,data=hysx_data).content

      #智能营销
      znyx_url='http://crm8.superboss.cc/marketing/saveMarketingActivityStrong'
      znyx_data = {'marketingStrongStr': json.dumps({"details":[{"content":u"【超级店长】亲爱的，店铺名周年遇上618，感谢有你相伴，好评荭包大派送，进店领取！ 退订回TD","memTitle":u"近半年店铺会员","id":"10010","type":"0","runEnd":"","runPoint":"","runStart":"","runType":"1","testMobile":"","jobName":u"即时","extra":"{\"sceneType\":\"\",\"sceneCrowdVal\":\"\",\"screenType\":2}",
                                                                 "sendTime":send_time}],
                                                     "conditionVOs":[{"blacklistMarketing":"","buyerNick":"","endBuyCount":"","endBuyFee":"","endDate":"2018-06-04","grade":"","groupIndexStr":"","limitDay":"1","receiverState":"","startBuyCount":"6","startBuyFee":"","startDate":"2017-12-06","setCf":"","specifycommodity":0,"numIid":""}],"jobName":"dssss","templateName":u"标准版","isTemplate":"false"}),
                   'api_name': 'saveMarketingActivityStrong'}
      print u"店长智能营销：%s" %session1.post(znyx_url,data=znyx_data).content


      #订单筛选发送
      ddsx_url='http://crm8.superboss.cc/orderSms/sendOrderSms?'
      ddsx_parmas={'message':u'【淘宝】亲爱的，拍下的交易剩下时间不多啦，即将要关闭了哦，喜欢的话抓紧时间付款，祝您购物愉快。 退订回TD',
            'sendTime':send_time,
            'mrnd':'0.27300120793478233',
            'sendCount':'1',
            'tidArr':'132981097559667403',
            'limitDay':'-1',
            'api_name': 'getFilterOrderList'}
      url2=ddsx_url+urlencode(ddsx_parmas)
      print u"店长订单筛选发送：%s" %session1.get(url2).content

      #指定号码发送
      zdhm_url='http://crm8.superboss.cc/marketing/sendManualMsg'
      zdhm_data={'isTest':'false',
      'sendTime':send_time,
      'phones':'18667047081',
      'msg':u'【多情g公子】亲爱的，拍下的交易剩下时间不多啦，即将要关闭了哦，喜欢的话抓紧时间付款，祝您购物愉快。 退订回TD',
      'api_name':'sendManualMsg'}
      print u"店长指定号码发送：%s" %session1.post(zdhm_url,data=zdhm_data).content

      # #上传文件发送号码(短信平台登录session)
      session2 = requests.session()
      dxpt_url = 'http://smsquick.superboss.cc/user/login'
      user_data = {'password': 'e10adc3949ba59abbe56e057f20f883e',
            'telephone': '18667047081'}
      session2.post(dxpt_url, data=user_data)
      wjdr_url='http://smsquick.superboss.cc/marketing/uploadFastSms'
      files = {'file': open(r'D:\LcsInterfaceAutomation\TestFiles\mobile.csv', 'rb')}
      data=json.loads(session2.post(wjdr_url,files=files).content)['data']
      filepath=data['filePath']
      filename=data['fileName']
      phonesize=data['phoneSize']
      uploadsize=data['uploadSize']
      dzpt_sendurl='http://smsquick.superboss.cc/marketing/sendFastSms?'
      parmas4={'filePath':filepath,
            'fileName':filename,
            'msg':u'【淘宝】亲爱的，拍下的交易剩下时间不多啦，即将要关闭了哦，喜欢的话抓紧时间付款，祝您购物愉快。 退订回TD',
            'phoneSize':phonesize,
            'sendTime':send_time,
            'limitday':'0',
            'uploadSize':uploadsize}
      dzpt_sendurl=dzpt_sendurl+urlencode(parmas4)
      print u"短信平台文件导入：%s" % session2.get(dzpt_sendurl).content
      # return u"店长会员筛选发送：%s" %session1.post(hysx_url,data=hysx_data).content,u"店长智能营销：%s" %session1.post(znyx_url,data=znyx_data).content
start_date='2018-07-05'
end_date='2018-07-15'
after_start=start_date.replace(start_date[-1],str(int(start_date[-1])+1))
after_end=end_date.replace(end_date[-1],str(int(end_date[-1])+1))
time1=start_date+' 23:40:39'
time2=after_start+' 00:20:55'
time3=after_start+' 02:44:23'
time4=after_start+' 23:55:57'
time5=end_date+' 23:40:39'
time6=after_end+' 00:20:55'
time7=after_end+' 02:44:23'
time8=after_end+' 23:55:57'
# aa=send_time(time1)

#验证超过22点仍可发送
print u"可以发送：%s\n\n"%send_time(time1),u"可以发送：%s\n\n"%send_time(time2),u"不可以发送：%s\n\n"%send_time(time3),u"可以发送：%s\n\n"%send_time(time4),u"可以发送：%s\n\n"%send_time(time5),u"可以发送：%s\n\n"%send_time(time6),u"不可以发送：%s\n\n"%send_time(time7),u"不可以发送：%s\n\n"%send_time(time8)


