# -*-coding:utf-8 -*-
import unittest,time
from Test_Case.order_care import Order_Care


class Crm_HomePage(unittest.TestCase):
    def setUp(self):
        self.fp = Order_Care()

    def test_crmhomepage(self):
        self.fp.creat_ordercare()

    def tearDown(self):
        pass
if __name__=='__main__':
    unittest.main()