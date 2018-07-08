#coding=utf-8
import requests,json
from Common.read_config import readconfig

url='http://sql.superboss.cc/query/doQueryObjectList'
header=readconfig('ray-authentication','header')
def select(sql):
    data={'pageNo':'1',
    'pageSize':'1000',
    'dbId':'18',
    'dbName':'',
    'schemaName':'s_crm',
    'url':'jconn2vygbspj.mysql.rds.aliyuncs.com',
    'sql':sql}
    r=json.loads(requests.post(url,data=data,headers=eval(header)).content)  #header从config里取出来是str，这里通过eval转换成dict，json.loads要求字符串参数必须用双引号
    return r

data=select('SELECT * FROM activity_gift_receive_info WHERE type=96 limit 100')
print data,len(data)
