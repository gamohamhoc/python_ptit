a,b = map(int,input().split())
mt=[]
import math
def check(i):
    if i<2: return False
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0:
            return False
    return True
for i in range(a):
    mt.append(list(map(int,input().split())))
for i in range(a):
    for j in range (b):
        if check(mt[i][j]):
            print(1,end=" ")
        else: print(0,end=" ")
    print()