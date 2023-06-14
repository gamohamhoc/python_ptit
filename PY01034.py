import math
import itertools
def cmp(a):
    return -a
for i in range(int(input())):
    s=str(input())
    m=itertools.permutations(s,len(s))
    m = sorted(m,reverse=True)
    check=0
    for j in m:
        kq=""
        for z in j:
            kq +=str(z)
            t=int(kq)
        if kq <s:
            if len(str(t))==len(s):
                check=1
                print(kq)
                break
    if check==0:
        print(-1)