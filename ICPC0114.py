import math
def check(a):
    if a < 2:
        return 0
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0: return 0
    return 1
n = int(input())
while n > 0:
    moi =0
    tong =0
    a = int(input())
    ktra =1
    if check(a) ==1:
        x =a
        while x > 0:
            m = x %10
            x = int(x/10)
            moi = moi*10+m
            tong +=m
            if check(m)==0:
                ktra =0
    else: ktra =0
    if check(tong)==0 or check(moi)==0:
        ktra =0
    if ktra ==1: print("Yes")
    else: print("No")
    n -=1
    