
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
print Fibonacci1(2)
print Fibonacci1(4)
print Fibonacci1(167)
    
def Fibonacci2(n):
    if (n==1):
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

print Fibonacci2(2)
print Fibonacci2(4)
print Fibonacci2(167)[2]

def Fibonacci3(n):
    phi = (1+5**0.5)/2 
    return int(round((phi**n - (1-phi)**n) / 5**0.5))

print Fibonacci3(2)
print Fibonacci3(4)
print Fibonacci3(167)


