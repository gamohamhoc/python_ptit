n = int(input())
ds = list(map(float,input().split()))
ds = sorted(ds)
l =0
r = len(ds)-1
while ds[l] == ds[0]:
    l += 1
while ds[r] == ds[len(ds)-1]:
    r -=1
tong =float(0)
dem = float(r - l+1)
while l<=r:
    tong += float(ds[l])
    l +=1
print(round(tong/dem,2))
