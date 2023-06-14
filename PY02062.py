import math
def check(dict):
    m=dict.values()
    for i in m:
        if i%2!=0:
            return False
    return True
def check1(ds,a):
    for i in range(0,len(ds)):
        dict={}
        j=i
        while j<len(ds) and j<i+a :
            if ds[j] not in dict:
                dict[ds[j]]=1
            else:
                dict[ds[j]] +=1
            j +=1
            if check(dict):
                return False
    return True
n = int(input())
while n>0:
    a=int(input())
    ds=list(map(int,input().split()))
    if check1(ds,a):
        print("YES")
    else:
        print("NO")
    n-=1