#coding=utf-8
from urllib import unquote
import requests,json
def params(params):
    data=dict([item.split('=') for item in params.split('&')])
    return data

print params('api_name=msgCheck_examineMsgContent&msgId=810826&examineType=2&appType=dianZhang&nick=tb511595_2013&message=%E3%80%90%E5%BA%97%E9%95%BF%E5%B0%8A%E4%BA%AB%E7%89%88%E3%80%91https%3A%2F%2F%C2%A0%E9%80%80%E8%AE%A2%E5%9B%9ETD&msgCount=1&date=2018-06-20+13%3A52%3A37')