import math
def check(a):
    for i in range(2,(int(math.sqrt(a)))+1):
        if a%i==0: return 0
    return 1
n = int(input())
while ( n> 0):
    a = str(input())
    s = int(len(a))
    x = ""+a[s-4]+a[s-3]+a[s-2]+a[s-1]
    so = int(x)
    if check(so)==1 and so > 1: print("YES")
    else: print("NO")
    n -=1