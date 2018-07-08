#coding=utf-8
import HTMLTestRunner
import datetime
import re
import sys
import time
import unittest

reload(sys)
sys.setdefaultencoding('utf-8')

def suite():
    suite=unittest.TestSuite()
    # file_dir='D:\LcsUiAutomation\TestSuitList'
    file_dir='D:\LcsInterfaceAutomation'
    discover=unittest.defaultTestLoader.discover(file_dir,
                                                 # pattern='test*.py',
                                                 pattern='testlink.py',
                                                 top_level_dir=None)    #找到文件下所有以test开头的文件 top_level_dir=None不去顶级目录
    for test_suite in discover:
        for test_case in test_suite:
            suite.addTests(test_case)                  #循环文件里的测试套件，再循环套件里的测试用例并添加到suite中
    return suite
if __name__ == '__main__':
#执行所有测试用例，并生成测试报告
    main=suite()
    runner=unittest.TextTestRunner()
    rq=''.join(re.findall('\d+',str(datetime.datetime.now())))
    # filepath ='D:\LcsUiAutomation\Test_Report\\'+'{0}.html'.format(rq)
    filepath ='D:\LcsInterfaceAutomation\Test_Report\\'+'{0}.html'.format(rq)
    fp = open(filepath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'测试报告',
                                           description=u'执行用例的情况')
    runner.run(main)
    time.sleep(40)
    fp.close()
# #将测试报告发送到邮箱
#     time.sleep(3)
#     send_email(filepath)