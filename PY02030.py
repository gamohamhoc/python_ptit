import math


def check1(a):
    for i in range (2,int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True
a = int(input())
ds = list(map(int,input().split()))
dict1={}
for i in ds:
    dict1[i]=1
tong =0
for i in dict1:
    tong += i[0]
tong1=0
check=0
for i in range(0,len(dict1)):
    tong1 += dict1[i][0]
    if check1(tong1) and check1(tong-tong1):
        print(i)
        check=1
        break
if check==0:
    print("NOT FOUND")