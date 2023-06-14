n = int(input())
ds = list(map(int,input().split()))
dem=0
for i in range(0,len(ds)-1):
    if ds[i] != ds[i+1]:
        dem +=1
print(dem)