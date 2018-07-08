#coding=utf-8
import requests,os,json,datetime
from time import sleep
from Common.read_config import readconfig


now_time = datetime.datetime.now().strftime('%Y-%m-%d')
d_time = datetime.datetime.strptime(now_time, '%Y-%m-%d')
time_one = datetime.timedelta(days=5)
end_time=datetime.datetime.strftime(d_time + time_one, '%Y-%m-%d')

numTid='https://item.taobao.com/item.htm?id=560034535843'

#催定金的data
data1={
'_includeItem':0,
'checkBlackList':False,
'endPrice':100,
'startPrice':1,
'endTime':21,
'startTime':9,
'orderSource':'JHS',
'orderFlag':1,
'openOrClose':1,
'setting':105,
'itemUrl':'',
'numTid':numTid,
'templateContent':'【京东】亲爱的， 还是您最有眼光，看中的是我家XX系列的限量款哦，来晚了就没有了哦，快快支付定金让他彻底属于您哦！@#店铺#u[1119705907](****(买家昵称))(****(买家姓名))(****(订单号)) (****(下单时间))  (****(订单详情)) 退订回TD',
'taskName':'林催定金',
'checkMemberFilter':'true',
'sendCoupon':False,
'startDateStr':now_time,
'endDateStr':end_time,
'receiveInfos':'上海,江苏,浙江',
'chooseMobile':'1',
'type':78,
'newTask':True,
'api_name':'saveMarketingSetting'}

#催尾款的data
data2={
'_includeItem':0,
'checkBlackList':False,
'endPrice':100,
'startPrice':1,
'endTime':21,
'startTime':9,
'orderSource':'JHS',
'orderFlag':1,
'openOrClose':1,
'setting':105,
'itemUrl':'',
'numTid':numTid,
'templateContent':'【京东】亲爱的， 还是您最有眼光，看中的是我家XX系列的限量款哦，来晚了就没有了哦，快快支付定金让他彻底属于您哦！@#店铺#u[1119705907](****(买家昵称))(****(买家姓名))(****(订单号)) (****(下单时间))  (****(订单详情)) 退订回TD',
'taskName':'林催尾款',
'checkMemberFilter':'true',
'sendCoupon':False,
'startDateStr':now_time,
'endDateStr':end_time,
'receiveInfos':'上海,江苏,浙江',
'chooseMobile':'0',
'type':79,
'newTask':True,
'api_name':'saveMarketingSetting'}

#催付的data
data3={
'_includeItem':0,
'checkBlackList':True,
'endPrice':100,
'startPrice':1,
'endTime':21,
'startTime':9,
'orderSource':'JHS',
'orderFlag':'3,4',
'openOrClose':1,
'setting':101,
'itemUrl':'',
'numTid':numTid,
'templateContent':'【淘宝】您好哦亲！看到您在我们店铺拍下的宝贝，库房已为您预留，如果方便的话请下午4点前及时付款，以免耽误给亲发货！淘宝愉快！天天好心情！ 退订回TD',
 'taskName':'林催付',
'checkMemberFilter':'true',
'sendCoupon':False,
'startDateStr':now_time,
'endDateStr':end_time,
'receiveInfos':'新疆,青海,云南,西藏',
'chooseMobile':'1',
'type':4,
'newTask':True,
'api_name':'saveMarketingSetting'}

#二次催付的data
data4={
'_includeItem':0,
'checkBlackList':True,
'endPrice':100,
'startPrice':1,
'endTime':21,
'startTime':9,
'orderSource':'',
'orderFlag':'1,2',
'openOrClose':1,
'setting':'24',
'itemUrl':'',
'numTid':numTid,
'templateContent':'【淘宝】您好哦亲！看到您在我们店铺拍下的宝贝，库房已为您预留，如果方便的话请下午4点前及时付款，以免耽误给亲发货！淘宝愉快！天天好心情！ u[1119705907](****(买家昵称))(****(买家姓名))(****(订单号)) (****(订单详情)) 退订回TD',
 'taskName':'林二次催付',
'checkMemberFilter':'false',
'sendCoupon':False,
'startDateStr':now_time,
'endDateStr':end_time,
'receiveInfos':'河南,广西,海南,辽宁,新疆,甘肃',
'chooseMobile':'1',
'type':8,
'newTask':False,
'api_name':'saveMarketingSetting'}

#付款的data
data5={
'_includeItem':0,
'checkBlackList':True,
'endPrice':100,
'startPrice':1,
'endTime':21,
'startTime':9,
'orderSource':'WAP',
'orderFlag':'1,2',
'openOrClose':1,
'setting':'',
'itemUrl':'',
'numTid':numTid,
'templateContent':'【淘宝】亲爱的(****(买家姓名))，感谢购买我们的商品！我们将随时播报状态，方便您随时了解。如有问题可以联系客服哦！ u[1119705907](****(买家昵称))(****(买家姓名))(****(订单号))(****(订单详情))(****(买家收货地址)) 退订回TD',
 'taskName':'林付款',
'checkMemberFilter':'false',
'sendCoupon':False,
'startDateStr':now_time,
'endDateStr':end_time,
'receiveInfos':'河南,广西,海南,辽宁,新疆,甘肃',
'chooseMobile':'1',
'type':9,
'newTask':False,
'api_name':'saveMarketingSetting'}

#发货的data
data6={
'_includeItem':0,
'checkBlackList':True,
'endPrice':100,
'startPrice':1,
'endTime':21,
'startTime':9,
'orderSource':'',
'orderFlag':'1,2',
'openOrClose':1,
'setting':'',
'itemUrl':'',
'numTid':numTid,
'templateContent':'【淘宝】主人，我已经乘坐小火箭开往您的所在地，快递确认包裹完好后再带我回家哦！ 退订回TD',
 'taskName':'林发货',
'checkMemberFilter':'false',
'sendCoupon':False,
'startDateStr':now_time,
'endDateStr':end_time,
'receiveInfos':'河南,广西,海南,辽宁,新疆,甘肃',
'chooseMobile':'1',
'type':1,
'newTask':True,
'api_name':'saveMarketingSetting'}

#延迟发货的data
data7={
'_includeItem':0,
'checkBlackList':True,
'endPrice':100,
'startPrice':1,
'endTime':21,
'startTime':9,
'orderSource':'WAP',
'orderFlag':'1,2',
'openOrClose':1,
'setting':'72',
'itemUrl':'',
'numTid':numTid,
'templateContent':'【淘宝】报告！您在u[1119705907]购买的宝贝经过连续3天通宵打包，店主已经昏迷不醒。等店主醒来就会立刻给亲发货，请亲耐心等待哟！ u[1119705907](****(买家昵称))(****(买家姓名))(****(订单号))(****(订单详情)) 退订回TD',
'taskName':'林延时发货',
'checkMemberFilter':'false',
'sendCoupon':False,
'startDateStr':now_time,
'endDateStr':end_time,
'receiveInfos':'河南,广西,海南,辽宁,新疆,甘肃',
'chooseMobile':'1',
'type':10,
'newTask':False,
'api_name':'saveMarketingSetting'}

#到货的data
data8={
'_includeItem':0,
'checkBlackList':True,
'endPrice':100,
'startPrice':1,
'endTime':21,
'startTime':9,
'orderSource':'',
'orderFlag':'1,2',
'openOrClose':1,
'setting':'',
'itemUrl':'',
'numTid':numTid,
'templateContent':'【淘宝】小主，是不是等急了，您的宝贝已经到达(****(收件人城市))，请保持手机畅通，方便伙计们与您联系，如果对宝贝不满意，我们一定会让你满意为止；当然如果感觉不错，请赏我们个5分好评。 退订回TD',
'taskName':'林到货',
'checkMemberFilter':'false',
'sendCoupon':False,
'startDateStr':now_time,
'endDateStr':end_time,
'receiveInfos':'河南,广西,海南,辽宁,新疆,甘肃',
'chooseMobile':'1',
'type':11,
'newTask':True,
'api_name':'saveMarketingSetting'}

#派件的data
data9={
'_includeItem':0,
'checkBlackList':True,
'endPrice':100,
'startPrice':1,
'endTime':21,
'startTime':9,
'orderSource':'',
'orderFlag':'1,2',
'openOrClose':1,
'setting':'',
'itemUrl':'',
'numTid':numTid,
'templateContent':'【淘宝】亲爱的，物流显示你朝思暮想的宝贝已经在派件中了喔，请你一定要注意查收，不要忘记TA噢，物流详情猛戳 (****(订单详情))! 退订回TD',
'taskName':'林派件',
'checkMemberFilter':'false',
'sendCoupon':False,
'startDateStr':now_time,
'endDateStr':end_time,
'receiveInfos':'河南,广西,海南,辽宁,新疆,甘肃',
'chooseMobile':'1',
'type':2,
'newTask':True,
'api_name':'saveMarketingSetting'}

#确认收货的data
data10={
'_includeItem':0,
'checkBlackList':True,
'endPrice':100,
'startPrice':1,
'endTime':8,
'startTime':9,
'orderSource':'',
'orderFlag':'1,2',
'openOrClose':1,
'setting':'100',
'itemUrl':'',
'numTid':numTid,
'templateContent':'【淘宝】亲，今天对于u[1119705907]来说是个特殊的日子，我们相识半个月了，感谢您的支持和加入。记得好评哦，我们每周上新哟~期待您的再次光临！ 退订回TD',
'taskName':'林确认收货',
'checkMemberFilter':'false',
'sendCoupon':False,
'startDateStr':now_time,
'endDateStr':end_time,
'receiveInfos':'河南,广西,海南,辽宁,新疆,甘肃',
'chooseMobile':'1',
'type':3,
'newTask':True,
'api_name':'saveMarketingSetting'}

#催评的data
data11={
'_includeItem':0,
'checkBlackList':True,
'endPrice':100,
'startPrice':1,
'endTime':21,
'startTime':9,
'orderSource':'',
'orderFlag':'1,2',
'openOrClose':1,
'setting':'6',
'itemUrl':'',
'numTid':numTid,
'templateContent':'【淘宝】尊敬的会员，听说您接收了我们家的宝贝，请问您是否满意呢？如果满意别忘了给我们一个5分好评噢，我们有新的优惠活动都会第一时间通知您！u[1119705907](****(买家昵称))(****(买家姓名))(****(订单号)) (****(订单详情)) 退订回TD',
'taskName':'林催评',
'checkMemberFilter':'false',
'sendCoupon':False,
'startDateStr':now_time,
'endDateStr':end_time,
'receiveInfos':'河南,广西,海南,辽宁,新疆,甘肃',
'chooseMobile':'1',
'type':69,
'newTask':False,
'api_name':'saveMarketingSetting'}

#好评关怀的data
data12={
'_includeItem':0,
'checkBlackList':True,
'endPrice':100,
'startPrice':1,
'endTime':21,
'startTime':9,
'orderSource':'',
'orderFlag':'1,2',
'openOrClose':1,
'setting':'101',
'itemUrl':'',
'numTid':numTid,
'templateContent':'【淘宝】我们的相遇不会因为评价而结束，有任何问题请随时联系我们，期待您的再次光临。 u[1119705907](****(买家昵称))(****(买家姓名))(****(订单号)) 退订回TD',
'taskName':'林好评关怀',
'checkMemberFilter':'false',
'sendCoupon':False,
'startDateStr':now_time,
'endDateStr':end_time,
'receiveInfos':'河南,广西,海南,辽宁,新疆,甘肃',
'chooseMobile':'1',
'type':107,
'newTask':False,
'api_name':'saveMarketingSetting'}

#退款关怀的data
data13={
'_includeItem':0,
'checkBlackList':True,
'endPrice':100,
'startPrice':1,
'endTime':21,
'startTime':9,
'orderSource':'',
'orderFlag':'1,2',
'openOrClose':1,
'setting':'',
'itemUrl':'',
'numTid':numTid,
'templateContent':'【淘宝】亲爱的(****(买家姓名))，已收到你的退款/退货申请。u[1119705907]将以最快的速度帮亲处理，有问题可随时联系售后。 u[1119705907](****(买家昵称))(****(买家姓名))(****(订单号))(****(订单详情)) 退订回TD',
'taskName':'林退款关怀',
'checkMemberFilter':'false',
'sendCoupon':False,
'startDateStr':now_time,
'endDateStr':end_time,
'receiveInfos':'河南,广西,海南,辽宁,新疆,甘肃',
'chooseMobile':'1',
'type':21,
'newTask':False,
'api_name':'saveMarketingSetting'}

DATA=[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13]
data_type = {
    'type': 77,
    'api_name': 'showOrderSetting'
            }
url_type=url='http://crm8.superboss.cc/sms/showOrderSetting'
class Order_Care(object):
    def __init__(self):
        self.headers = readconfig('TEST_HEADERS', 'HEADERS')
        self.url=readconfig('TEST_HEADERS','ORDERCARE_URL')
    def creat_ordercare(self):
        status = 0
        for data in DATA:
            settingId=json.loads(requests.post(self.url,data=data,headers=self.headers).content)['data']['settingId']
            print settingId
            while status!=1:
                cf_list=json.loads(requests.post(url_type,data=data_type,headers=self.headers).content)['data']['list']
                for i in cf_list:
                    setid=i['settingId']
                    if setid==settingId:
                        status=i['status']
                        sleep(10)
            else:
                print('任务已开启')









