nto=[]
import math
for i in range(2,10000):
    check =0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            check =1
            break
    if check ==0:
        nto.append(i)
a = int(input())
ds = list(map(int,input().split()))
tong =0
for i in ds:
    x = abs (i-min(nto,key=lambda n: abs(n-i)))
    tong =max (tong,x)
print(tong)
