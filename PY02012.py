a = int(input())
ds = list(map(int,input().split()))
chan =[]
le=[]
for i in ds:
    if i%2 ==0:
        chan.append(i)
    else:
        le.append(i)
chan = sorted(chan)
le = sorted(le,key=lambda x: -x )
for i in range(0,a):
    if ds[i] %2 ==0:
        print(chan[0],end=" ")
        del chan[0]
    else:
        print(le[0],end=" ")
        del le[0]
