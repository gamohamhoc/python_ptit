import math
a,b = map(int,input().split())
ds =[]
print(b,end=" ")
for i in range(2,10002):
    check=0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0: 
            check =1
            break
    if i>=2 and check==0:
        ds.append(i)
for i in range(0,a):
    print(b+ds[i],end=" ")
    b = b + ds[i]
print()
