import math
n= int(input())
def ucln(a,b):
    if b ==0: return a
    else: return ucln(b, a % b)
def check (a):
    for i in range(2 , int(math.sqrt(a))+1):
        if a % i == 0 : return 1
    return 0
while n > 0:
    x = int(input())
    dem =0
    for i in range(1,x):
        if ucln (i,x) == 1 :
            dem += 1
    if dem > 1 and check (dem) == 0: print("YES")
    else: print("NO")
    n -= 1
