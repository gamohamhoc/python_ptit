import math
def check(a,b):
    for i in range(2,int(math.sqrt(a))+1):
        if b%i ==0 and a %i ==0:
              return False
    return True
n = int(input())
ds = list(map(int, input().split()))
ds = sorted(ds)
for i in range(0,len(ds)-1):
    for j in range(i+1,len(ds)):
        if check(ds[i],ds[j]):
                    print(ds[i],ds[j])