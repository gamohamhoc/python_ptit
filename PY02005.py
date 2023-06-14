n = int(input())
ds = list(map(int,input().split()))
dem=0
for i in range(0,len(ds)-1):
    for j in range(i+1,len(ds)):
        if ds[i] > ds[j]:
            dem +=1
print(dem)