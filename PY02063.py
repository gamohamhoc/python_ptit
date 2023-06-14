a= int(input())
ds=list(map(int,input().split()))
Max=0
ds=sorted(ds)

Max=max(ds[0]*ds[1]*ds[len(ds)-1],ds[len(ds)-1]*ds[len(ds)-2]*ds[len(ds)-3],ds[0]*ds[1],ds[len(ds)-1]*ds[len(ds)-2])
print(Max)
