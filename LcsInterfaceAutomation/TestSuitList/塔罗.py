#coding=utf-8
from time import sleep
from datetime import datetime
a=[]
for i in range(1,5):
    a.append(i)
b=[]
c=[]
count=0
def move(n,a, b, c):
    global count
    if n ==1:
        c.append(a[-1])
        a.pop()
        print(a, '-->', c)
        count+=1
    else:
        move(n-1, a, c, b)
        c.append(a[-1])
        a.pop()
        print(a, '-->', c)
        count+=1
        move(n-1, b, a, c)
print datetime.now()
move(4,a,b,c)
print count,datetime.now()


