#coding=utf-8
import xlwt,xlrd,requests,time,sys
from xlutils.copy import copy
from Common.logger import Logger
import ConfigParser
from urllib import urlencode
from Common import get_cookie
from read_config import readconfig

reload(sys)
sys.setdefaultencoding('utf-8')

class ExcelHanding1(object):
    def __init__(self):
        self.session=get_cookie.Get_Cookie('tb511595_2013')[0]

#读取文件，这里可以判断一下文件是否能打开（路劲和文件是否存在）
    def readxlsx(self,filename):
        case_list=[]
        try:
            data=xlrd.open_workbook(filename)
            self.WB=copy(data)
            self.WS_SHEET1=self.WB.get_sheet(0)
            self.WS_SHEET2=self.WB.get_sheet(1)
            sheet = data.sheet_by_index(0)
            rows = sheet.nrows
            for i in range(1,rows):
                case_list.append(sheet.row_values(i))
        except Exception as f:
            print(f)
        return case_list

#写入表格sheet1和sheet2
    def write(self,filename):
        pass_count=0
        unpass_count=0
        self.fp=ExcelHanding1()
        CASE=self.fp.readxlsx(filename)
        for i,case in enumerate(CASE,1):
            if case[4]=='post':
                r=self.session.post(case[5],data=eval(case[6]))
            elif case[4]=='get':
                get_url=case[5]+'?'+urlencode(eval(case[6]))
                r=self.session.get(get_url)
            elif case[4]=='put':
                if case[5]=='':
                    r = self.session.get(case[5])
                else:
                    r = self.session.put(case[5],data=eval(case[6]))
            else:
                r = self.session.delete(case[5])
            result=r.content.decode('utf-8')
            self.fp.WS_SHEET1.write(i, 8, result)
            if case[7] in result:
                print(u'通过')
                self.fp.WS_SHEET1.write(i,9,u'通过',xlwt.easyxf('pattern: pattern solid, fore_colour bright_green; font: bold on;'))
                pass_count+=1
            else:
                print(u'不通过')
                self.fp.WS_SHEET1.write(i,9,u'不通过',xlwt.easyxf('pattern: pattern solid, fore_colour red; font: bold on;'))
                unpass_count+=1
        self.fp.WS_SHEET2.write(1,1,pass_count)
        self.fp.WS_SHEET2.write(2, 1, unpass_count)
        self.fp.WS_SHEET2.write(3, 1, unpass_count+pass_count)
        try:
            self.fp.WS_SHEET2.write(4, 1, '{0}%'.format(round(pass_count/(unpass_count+pass_count),4)*100))
        except ZeroDivisionError:
            pass
        self.fp.WB.save(filename)