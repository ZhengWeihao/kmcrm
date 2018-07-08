#-*-coding=utf-8-*-
import ConfigParser

def readconfig(section,option):
    config = ConfigParser.ConfigParser()
    file_path = r'D:\LcsInterfaceAutomation\Config\config.ini'
    config.read(file_path)
    return config.get(section,option)

# data1={"grade":"0 1 2 3 4","needPhone":"needPhone","minBuyCount":"1","status":0,"taobaoId":1119705907}
#
# data2={"grade":"0 1 2 3 4","lastMsgTime":"2018-06-01 15:36:07","minBuyCount":"1","status":0,"taobaoId":1119705907}
# url='http://dzcrm.superboss.cc/marketing/testQueryMember?'
# url=url+urlencode(data2)
# print url
