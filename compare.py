# -*- coding: cp936 -*-
from fibonacci import Fibonacci1, Fibonacci2
from time import time
n = [10,100,1000,10000,100000,1000000]
timeA = []
timeB = []
for number in n:
    temp = 0
    temp2 = 0
    for i in range(10):
        start = time()
        Fibonacci1(number)
        stop = time()
        time1 = stop-start
        temp = temp + time1
        start2 = time()
        Fibonacci2(number)
        stop2 = time()
        time2 = stop2-start2
        temp2 = temp2 + time2
    temp = temp/10.0
    timeA.append(temp)
    temp2 = temp2/10.0
    timeB.append(temp2)


print timeA
print timeB
