n = int(input())
while n > 0:
    a,b = map(int,input().split())
    hien =""
    if b < 100000:
        ds=[0,0,0,0,0,0,0,0,0,0]
    else:
        ds=[38894, 50001 ,50000 ,50000 ,50000, 50000 ,50000, 50000, 50000 ,50000]
    for i in range(a,b+1):
        hien = hien + str(i)
    for i in range(0,10):
        x= str(i)
        ds[i]+=hien.count(x)
    for i in ds:
        print(i,end=" ")
    print()
    n-=1