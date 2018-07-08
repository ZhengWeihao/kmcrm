#-*-coding=utf-8-*-
import requests,json,re
from Common.dianzhang_login import CRM_session

session=CRM_session('tb511595_2013')

#校验插入淘口令功能
print u'插入淘口令：'
tk_url='http://crm8.superboss.cc/tkl/getTkl'
tk_goods_data={'commodityPicUrl': 'https://img.alicdn.com/bao/uploaded/i3/1119705907/TB2WK5xoDlYBeNjSszcXXbwhFXa_!!1119705907.jpg',
         'commodityTitle': u'小曼专属',
         'couponId': '',
         'customUrl': '',
         'numIid': '568669622633',
         'shopHomeUrl': '',
         'text': '',
         'tklType': '1',
         'api_name': 'getTkl'
         }
tk_shop_data={'commodityPicUrl': '',
         'commodityTitle': '',
         'couponId': '',
         'customUrl': '',
         'numIid': '',
         'shopHomeUrl': 'https://shop268814631.taobao.com/',
         'text': '',
         'tklType': '2',
         'api_name': 'getTkl'
         }
tk_coupon_data={'commodityPicUrl': '',
         'commodityTitle': '',
         'couponId': '1277710877',
         'customUrl': '',
         'numIid': '',
         'shopHomeUrl': '',
         'text': '',
         'tklType': '3',
         'api_name': 'getTkl'
         }
tk_custom_data={'commodityPicUrl': '',
         'commodityTitle': '',
         'couponId': '',
         'customUrl': 'https://smf.taobao.com/index.htm?menu=yhkq&module=yhkq',
         'numIid': '',
         'shopHomeUrl': '',
         'text':u'接口',
         'tklType': '4',
         'api_name': 'getTkl'
         }
Tk_data=[tk_goods_data,tk_shop_data,tk_coupon_data,tk_custom_data]
for tk_data in Tk_data:
    try:
        assert re.findall(u'€.*?€',json.loads(session.post(tk_url,tk_data).content)['data']['tkl'])
        print u'正确'
    except Exception as e:
        print u'不正确：%s'%e

#校验生成短链的功能
print u'生成短链：'
short_url='http://crm8.superboss.cc/sms/getShortUrl'
short_goods_data={'shortUrlType':'0',
                 'shortUrlName':'1529215698922',
                 'longUrl':'https://item.taobao.com/item.htm?id=568669622633',
                 'api_name':'getShortUrl'}
short_shop_data={'shortUrlType':'1',
                 'shortUrlName':'1529215840652',
                 'longUrl':'https://shop268814631.taobao.com/',
                 'api_name':'getShortUrl'}
short_coupon_data={'shortUrlType':'2',
                 'shortUrlName':'1529215889226',
                 'longUrl':'https://taoquan.taobao.com/coupon/unify_apply.htm?sellerId=1119705907&activityId=9ccf2d5801c64e1ca8e18c02b7c603da',
                 'api_name':'getShortUrl'}
short_custom_data={'shortUrlType':'1',
                 'shortUrlName':'1529215933313',
                 'longUrl':'https://smf.taobao.com/index.htm?menu=yhkq&module=yhkq',
                 'api_name':'getShortUrl'}
Short_data=[short_goods_data,short_shop_data,short_coupon_data,short_custom_data]
for short_data in Short_data:
    try:
        assert re.findall('c.tb.cn/c..*?',json.loads(session.post(short_url,short_data).content)['data']['url'])
        print u'正确'
    except Exception as e:
        print u'不正确：%s'%e

