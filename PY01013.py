n =int(input())
import math
def ucln(a,b):
    if b ==0: return a
    else: return ucln(b,a%b)
def check(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i ==0: return 0
    return 1
while n > 0 :
    a,b = map(int,input().split())
    c = ucln (a,b)
    tong = 0
    while c > 0 :
        tong += c%10
        c = int(c/10)
    if tong > 1 and check(tong) == 1: print("YES")
    else: print("NO")
    n -= 1
