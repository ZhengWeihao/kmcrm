#coding=utf-8
import requests,json,datetime,sys
from time import sleep
from urllib import urlencode
from Common import get_cookie,dianzhang_login

reload(sys)
sys.setdefaultencoding('utf-8')
send_Time=(datetime.datetime.now()+datetime.timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')

class Group_send():
    def __init__(self):
        self.session = dianzhang_login.CRM_session('tb511595_2013')

    # 查看群发记录查询，{手动发送type：0，筛选发送type：1，订单筛选type：99，智能营销type：2000，订单分析type：3，手动催尾款type,4，会员权益type：1，手动催好评type：5}
    # 会员权益-群发记录查询url='http://crm8.superboss.cc/marketing/sendMsgRecord?start=2017-12-19&end=2018-01-11&pageNo=1&pageSize=10&type=1&isCoupon=true&api_name=sendMsgRecord'多了个iscoupon=true
    def send_log(self,type):
        group_send_url = 'http://crm8.superboss.cc/marketing/sendMsgRecord?start=2017-12-18&end=2018-11-10&pageNo=1&pageSize=10&type={0}&api_name=sendMsgRecord'.format(type)
        group_send=json.loads(self.session.get(group_send_url).content)['data']['list'][0]
        i=20
        print group_send['gmtEnd'],group_send['status']
        if group_send['gmtEnd'] == send_Time:
            while i>1:
                if group_send['status'] != 20:
                    print '仍未发送，等待3秒'
                    group_send = json.loads(self.session.get(group_send_url).content)['data']['list'][0]
                    sleep(3)
                    i=i-1
                else:
                    break
        else:
            print  u'未生成群发记录'

    # 查看短信发送记录，{短信群发selType：5，催付提醒selType：4，二次催付selType：8，已付款关怀selType：9，发货提醒selType：1，延迟发货selType：20，派件提醒selType：2，到货提醒：11，
    # 确认收货提醒selType：3，退款关怀-买家申请退款selType：21，退款关怀-退款成功selType：42，退款关怀-同意退款selType:40，退款关怀-拒绝退款selType：41，睡眠提醒selType：43，
    # 退款预警selType：45，物流异常预警selType：46，会员升级提醒-（买家->普通会员）selType：47，会员升级提醒-（普通会员->高级会员）selType：48，会员升级提醒-（高级会员->VIP会员）selType：49，
    # 会员升级提醒-（VIP会员->至尊VIP）selType：50，消息提醒selType：53，订单筛选发送selType：117，好评关怀selType：107，活动催付selType：58，催评提醒selType：69，订单分析selType：96，
    # 预售催付-催定金selType：78，预售催付-催尾款selType：79，交易管理selType：120，手动催尾款selType：101，手动催好评selType：102}
    def send_record(self,type):
        msg_send_url = 'http://crm8.superboss.cc/marketing/sendMsgDetail?buyerNick=&end=&pageNo=1&pageSize=10&phone=&selType={0}&start=2017-12-18&thisSearchBak=false&api_name=sendMsgDetail'.format(type)
        msg_send = json.loads(self.session.get(msg_send_url).content)['data']['list'][0]
        try:
            assert msg_send['sendTime'] >= send_Time
            print u'已提交到短信通道'
        except AssertionError:
            print u'未提交到短信通道'

    # 订单查询接口请求  {近22天订单：'' ，代付款：WAIT_BUYER_PAY ，待发货：WAIT_SELLER_SEND_GOODS ，已发货： WAIT_BUYER_CONFIRM_GOODS ，
    # 退款中：REFUNDING ，交易成功：TRADE_FINISHED ，交易关闭 ：TRADE_CLOSED}
    def order_search(self, status):
        order_search_url = 'http://crm8.superboss.cc/orderSms/getOrderList?pageSize=10&consignTimeEnd=&consignTimeStart=&createdEnd=&createdStart=&limitDay=-1&paymentEnd=&paymentStart=&buyerNick=&refundStatus=&sellerFlag=&tradeFrom=&receiverState=&status={0}&pageNo=1&api_name=getFilterOrderList'.format(
            status)
        order_search = json.loads(self.session.get(order_search_url).content)['result']
        try:
            assert order_search == '1'
        except AssertionError:
            print u"订单状态查询错误"

    # 手动发送的接口请求
    def manual_input(self):
        input_url = 'http://crm8.superboss.cc/marketing/sendManualMsg'
        data={'isTest':'false',
        'sendTime':send_Time,
        'phones':'15655511595',
        'msg':u'【超级店长】最后两次 退订回TD',
        'api_name':'sendManualMsg'
        }
        input_result=json.loads(self.session.post(input_url,data=data).content)['result']
        try:
            assert input_result=='1'
        except AssertionError as f:
            print u'手动输入发送失败'

    #订单筛选发送接口请求
    def order_send(self,order_number):
        order_base_url='http://crm8.superboss.cc/orderSms/sendOrderSms?'
        data={
            'tidArr': order_number,
            'message':u'【淘宝】我们不常提起，却从未忘记。双十二备下的厚礼已经向您飞奔！请静候. 退订回TD',
            'sendCount': '1',
            'sendTime': send_Time,
             'limitDay':'-1',
            'api_name':'getFilterOrderList'
              }
        order_send_url=order_base_url+urlencode(data)
        order_result=json.loads(self.session.get(order_send_url).content)['result']
        try:
            assert order_result == '1'
        except AssertionError as f:
            print u'订单筛选发送失败'

    # 会员筛选发送接口请求
    def vip_select_send(self):
        vip_select_url='http://crm8.superboss.cc/marketing/sendMsg'
        data={
            'buyerNick':u'流氓大人55',
            'blacklistMarketing':'',
            'endBuyCount':'',
            'endBuyFee':'',
            'endDate':'',
            'grade':'',
            'groupIndexStr':'',
            'limitDay':'1',
            'numIid':'',
            'receiverName':'',
            'receiverState':'',
            'specifycommodity':'0',''
            'startBuyCount':'',
            'startBuyFee':'',
            'startDate':'',
            'realCount':'1',
            'testMobile':'',
            'sendTime':'',
            'msg':u'【超级店长】年度最后一次大.促即将开始，你还在犹豫什么？双十二给你一击即中的巨蕙，u[1119705907]，不见不散。 退订回TD',
            'api_name':'sendMsg'
              }
        vip_select=json.loads(self.session.post(vip_select_url,data=data).content)['result']
        try:
            assert vip_select=='1'
        except AssertionError:
            print u'会员筛选发送失败'

    # 优惠券发送接口请求
    def send_coupon(self):
        send_coupon_url='http://crm8.superboss.cc/coupon/sendCouponAndMsg'
        data={
            'receiverName': '林春生',
            'blacklistMarketing': '1',
            'specifycommodity': '0',
            'grade': '1, 2, 3, 4',
            'limitDay':'-1',
            'api_name':'queryMember',
            'msg':'【淘宝】亲爱的XX会员, 3月19日新品10:00准时上架哟，新势力周给力活动尽在u[1119705907]退订回TD',
            'mrnd':'0.029217131986520428',
            'sendCount':'1',
            'couponId':'1265278854'
        }
        coupon=json.loads(self.session.post(send_coupon_url,data=data).content)['result']
        try:
            assert coupon=='1'
        except AssertionError:
            print u'优惠券发送失败'

    #获取剩余短信接口请求
    def balance(self):
        balance_url='http://duanxinhttp.superboss.cc/balance2.jsp'
        balance_data={'taobaoId':'1119705907',
                      'sign':'e27ee22e279634af97a46ad51fa8e046'}
        balance=json.loads(self.session.post(balance_url,data=balance_data).content)['restMsgCount']
        return balance

    #活动订单列表已发送条数接口请求
    def have_send(self,order_number):
        have_send_url='http://crm8.superboss.cc/orderSms/getOrderList?'
        parmas={'pageSize':'10',
                'limitDay':'-1',
                'pageNo':'1',
                'api_name':'getFilterOrderList'
                }
        have_send_url=have_send_url+urlencode(parmas)
        have_send_oid=json.loads(self.session.get(have_send_url).content)['data']['tradeList']
        for oid in have_send_oid:
            if oid['orderList'][0]['oid'].encode("gbk")==order_number:
                return oid['sendMsgCount']

order_number = '101619255195255037'
#实例化对象
A=Group_send()

#获取当前剩余短信和订单已发送数
sendMsgCount=A.have_send(order_number)
balance=A.balance()
print sendMsgCount,balance

#订单发送
A.order_send(order_number)

#查看群发记录和发送日志
A.send_log('99')
A.send_record('117')
print A.have_send(order_number),A.balance()

#判断短信剩余条数是否减少和订单已发送条数是否增加
if int(A.have_send(order_number))==int(sendMsgCount)+1 and int(A.balance())==int(balance)-1:
    print '测试通过'
























