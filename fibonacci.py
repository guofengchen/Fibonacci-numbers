# -*- coding: cp936 -*-
from time import time

def Fibonacci1(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        F= []
        F.append(0)
        F.append(1)
        for i in range(n-1):
            temp=F[0]+F[1]
            F[0]=F[1]
            F[1]=temp

    return F[1]
   
def Fibonacci2(n):
    if (n==0):
        return [1,0,0,1]
    elif (n==1):
        return [1,1,1,0]
    else:
        [a,b,c,d] = Fibonacci2(n/2)
        newa = a**2 + b*c
        newb = a*b + b*d
        newc = a*c + c*d
        newd = b*c + d**2
        if n%2 ==1:
            [tempa,tempb,tempc,tempd] = [newa,newb,newc,newd]
            newa = tempa + tempb
            newb = tempa
            newc = tempc + tempd
            newd = tempc
        return [newa,newb,newc,newd]

def power(phi,n):
    if(n==0):
        return 1
    if(n==1):
        return phi
    else:
        temp = power(phi,n/2)**2
        if n%2==1:
            temp = temp*phi
        return temp

def Fibonacci3(n):
    phi = (1+5**0.5)/2
    temp = power(phi,n)/5**0.5
    return int(round(temp))

def Fibonacci4(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return Fibonacci4(n-1)+ Fibonacci4(n-2)



def main():
    n = input("input n for Fibonacci calculate:")
    print "Bottom-up method:"
    start = time()
    print("Start: " + str(start))
    ans1 = Fibonacci1(n)
    stop = time()
    print("Stop: " + str(stop))
    print(str(stop-start) + "秒")
    print ans1
    print "Recursive squaring method:"
    start = time()
    print("Start: " + str(start))
    ans2 = Fibonacci2(n)[2]
    stop = time()
    print("Stop: " + str(stop))
    print(str(stop-start) + "秒")
    print ans2
    exit = input("Press any key to exit.")
'''
    print "Naive recursive squaring method:"
    start = time()
    print("Start: " + str(start))
    ans3 = Fibonacci3(n)
    stop = time()
    print("Stop: " + str(stop))
    print(str(stop-start) + "秒")
    print ans3
    print "Naive recursive algorithm:"
    start = time()
    print("Start: " + str(start))
    ans4 = Fibonacci4(n)
    stop = time()
    print("Stop: " + str(stop))
    print(str(stop-start) + "秒")
    print ans4
'''  
if __name__=='__main__':
    main()
    
