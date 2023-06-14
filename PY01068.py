import itertools
a,b = map(int,input().split())
ds=list(map(str,input().split()))
ds=sorted(ds)
dict={}
for i in ds:
    dict[i]=1
ds1=itertools.combinations (dict,b)
for i in ds1:
    for j in i:
        print(j,end=" ")
    print()