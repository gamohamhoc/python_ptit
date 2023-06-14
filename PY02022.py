a =int(input())
import math
def check(a):
    if a<2: return False
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True
ds = list(map(int,input().split()))
dict={}
for i in ds:
    if check(i):
        if i not in dict:
            dict[i]=1
        else:
            dict[i] +=1
for i in dict:
    print(i,dict[i])