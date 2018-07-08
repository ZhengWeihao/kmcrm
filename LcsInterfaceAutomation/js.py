#coding=utf-8
import os,subprocess
from subprocess import Popen,PIPE
import requests


# 执行本地的js
# os.system(r"python D:\LcsInterfaceAutomation\testlink.py")
p=Popen(r"python D:\LcsInterfaceAutomation\testlink.py", stdout=PIPE, stderr=PIPE)
p.wait()
if(p.returncode == 0):
    print "stdout:%s" %p.stdout.read()








    、
