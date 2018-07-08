#coding=utf-8
import requests,json

class Requests(object):
    def __init__(self):
     self.requests=requests.session()

    #GET请求
    def requests_get(self,url,headers):
     self.requests.get(url,headers=headers)

    #POST请求
    def requests_post(self,url,data,headers):
     self.requests.post(url,data=data,headers=headers)

    #PUT请求
    def requests_put(self,url,data,headers):
     self.requests.put(url,data=data,headers=headers)

    #DELETE请求,
    def requests_delete(self, url, data, headers):
     self.requests.delete(url,headers=headers)

