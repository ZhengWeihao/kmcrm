# -*-coding:utf-8 -*-
import unittest,time,sys
from Common.Excel_Handing1 import ExcelHanding1


class Crm_HomePage(unittest.TestCase):
    def setUp(self):
        self.fp = ExcelHanding1()

    def test_crmhomepage(self):
        self.fp.write(u'D:\LcsInterfaceAutomation\CASE_EXCEL\测试用例.xlsx')

    def tearDown(self):
        pass
if __name__=='__main__':
    unittest.main()