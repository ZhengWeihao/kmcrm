# -*- coding: utf-8 -*-
'''
将日志存入到指定的文件中,并指定保存日志的文件路径，日志级别，以及调用文件
'''


import logging,os,datetime,re

class Logger(object):
    def __init__(self, logger):
        # 创建一个logger
        self.logger = logging.getLogger(logger)   # logger参数为log的输出名称
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        log_path = 'D:\LcsUiAutomation\ERROE_Logs'  # 项目根目录下/Logs 保存日志
        rq=datetime.datetime.now().strftime('%Y%m%d%H')
        # rq = ''.join(re.findall('\d+', str(datetime.datetime.now())))
        log_name = log_path + '\{0}.log'.format(rq)
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def getlog(self):
        return self.logger
