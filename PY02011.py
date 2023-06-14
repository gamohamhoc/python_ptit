a = int(input())
ds = list(map(int,input().split()))
tong= 1e9
luu=0
for i in range(0,len(ds)):
    x=0
    for j in range(0,len(ds)):
        x += abs(ds[i]-ds[j])
    if tong >  x:
        tong =x
        luu =ds[i]
print(tong,luu)
