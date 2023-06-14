import math
a=int(input())
ds=list(map(int,input().split()))
ds=sorted(ds)
for i in range(0,len(ds)-1):
    for j in range(i+1,len(ds)):
        if math.gcd(ds[i],ds[j])==1:
            print(ds[i],ds[j])