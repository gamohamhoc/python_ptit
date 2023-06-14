n = int(input())
ds = [1,1,2]
for i in range(3,93):
    ds.append(ds[i-1]+ds[i-2])
while n > 0:
    a,b = map(int,input().split())
    for i in range(a-1,b):
        print(ds[i],end=" ")
    n -=1