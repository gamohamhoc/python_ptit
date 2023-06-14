import math
while 1:
    a,b,c,d = map(int,input().split())
    if (a==b and b ==c and c==d and d==0):
        break
    dem=0
    while a!=b or b !=c or c!=d:
        x = a
        a = abs(a-b)
        b = abs(b-c)
        c = abs(c-d)
        d = abs(d-x)
        dem +=1
    print(dem)

    