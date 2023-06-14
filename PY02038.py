a = int(input())
mt=[]
import itertools
import math
def so_to_hop(a,b):
    x=math.factorial(a)
    y=math.factorial(b)
    z=math.factorial(abs(a-b))
    return x/(y*z)
for i in range(a):
    mt.append(list(map(str,input().split())))
dem=0
for i in mt:
    hien = str(i)
    cham=0
    for j in hien:
        if j =='C':
            cham +=1
    dem += so_to_hop(cham,2)
cham=0

for i in range(a):
    hien =""
    cham=0
    for j in mt:
        moc = str(j)
        hien = hien + moc[i+2]
    for j in hien:
        if j =='C':
            cham +=1
    dem += so_to_hop(cham,2)
print(int(dem))
        
        