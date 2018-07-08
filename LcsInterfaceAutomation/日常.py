#coding=utf-8
import time,datetime,requests,json,sys,ConfigParser,re
from urllib import urlencode
from time import ctime,sleep
from Common import get_cookie,dianzhang_login
import xlwt,xlrd,requests,time,sys
from xlutils.copy import copy
from Common.logger import Logger
import ConfigParser
from urllib import urlencode
from Common import get_cookie

name=int(time.time()*1000)   #当前时间戳有13位，如果字数限制直接取n个str(now_time)[-n:]
start_time=(datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')  #开始时间
end_time=(datetime.datetime.now()+datetime.timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')    #结束时间
startTime=int(time.mktime(time.strptime(start_time, "%Y-%m-%d %H:%M:%S"))*1000)
endTime=int(time.mktime(time.strptime(end_time, "%Y-%m-%d %H:%M:%S"))*1000)
session=dianzhang_login.CRM_session('tb511595_2013')
url='http://dzcrm.superboss.cc/points/activity/create'
data={"endTime":endTime,"startTime":startTime,"grades":[-1,0,1,2,3,4],"isShow":"true","name":"da444","pointSetting":{"0":"1","1":"1","2":"1","3":"1","4":"1","-1":"1"},"ruleDescription":"活动时间：{0}- {1}\n参与人员：非会员、店铺会员、普通会员、高级会员、VIP会员、至尊VIP\n积分设置：非会员1个积分、店铺会员1个积分、普通会员1个积分、高级会员1个积分、VIP会员1个积分、至尊VIP1个积分\n签到递增奖励：第2天开始，每天额外增加2个积分，连续增加1天后不再增加。".format(start_time,end_time),"type":"sign","increaseReward":{"pointsPerDay":"2","dayToGive":"1"},"skinType":"standard"}
print session.post(url,data=json.dumps(data)).content

# url='http://crm8.superboss.cc/points/shop/updateSettings'
# data={"pointPrice":"3","pointsSettingConsume":{"upperLimit":"30"},"sendValueType":"1","pointStatus":1,"gradeSort":{"shopCustomer":"2","normalMember":"3","seniorMember":"7.7","vipMember":"10","extremeMember":"0.1"}}
# # print session.post(url,json=data).content
dt='2018-06-06 14:10:14'
a=time.strptime(dt, "%Y-%m-%d %H:%M:%S")
print int(time.mktime(a)*1000)
# print int(time.time()*1000)

# data=xlrd.open_workbook(u'D:\LcsInterfaceAutomation\CASE_EXCEL\测试用例.xlsx')
# WB=copy(data)
# WS_SHEET1=WB.get_sheet(0)
# WS_SHEET2=WB.get_sheet(1)
# sheet = data.sheet_by_index(0)
# a=sheet.cell(1,6).value
# session=dianzhang_login.CRM_session('tb511595_2013')
# url='http://crm8.superboss.cc/marketing/queryMember'
# data={'limitDay':'1','specifycommodity':'0','returnValue':'true','pageNo':'1','pageSize':'10'}
# print session.get(url,data=json.dumps(data)).content