#coding=utf-8
import xlwt,xlrd,requests,time,sys
from xlutils.copy import copy
from Common.logger import Logger
import ConfigParser
from read_config import readconfig

reload(sys)
sys.setdefaultencoding('utf-8')

class ExcelHanding(object):
    def __init__(self):
        self.headers=readconfig('TEST_HEADERS','HEADERS')

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
            return case_list
        except Exception as f:
            print(f)

#写入表格sheet1和sheet2
    def write(self,filename):
        pass_count=0
        unpass_count=0
        self.fp=ExcelHanding()
        CASE=self.fp.readxlsx(filename)
        for i,case in enumerate(CASE,1):
            if case[3]=='post':
                r=requests.post(case[4],data=eval(case[5]),headers=eval(self.headers))
            elif case[3]=='get':
                r=requests.get(case[4],headers=eval(self.headers))
            elif case[3]=='put':
                if case[5]=='':
                    r = requests.get(case[4], headers=eval(self.headers))
                else:
                    r = requests.put(case[4],data=eval(case[5]), headers=eval(self.headers))
            else:
                r = requests.delete(case[4], headers=eval(self.headers))
            result=r.content.decode('utf-8')
            self.fp.WS_SHEET1.write(i, 7, result)
            if case[6] in result:
                print('通过')
                self.fp.WS_SHEET1.write(i,8,u'通过')
                pass_count+=1
            else:
                print('不通过')
                self.fp.WS_SHEET1.write(i, 8,u'不通过')


                unpass_count+=1
        self.fp.WS_SHEET2.write(1,1,pass_count)
        self.fp.WS_SHEET2.write(2, 1, unpass_count)
        self.fp.WS_SHEET2.write(3, 1, unpass_count+pass_count)
        self.fp.WS_SHEET2.write(4, 1, '{0}%'.format(round(pass_count/(unpass_count+pass_count),4)*100))
        self.fp.WB.save(filename)
