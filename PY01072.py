import itertools
a,b = map(int,input().split())
ds= list(map(int,input().split()))
dict={}
for i in ds:
    dict[i]=1
ds1=dict
ds1=sorted(ds1)
ds2=itertools.combinations(ds1,b)
for i in ds2:
    for j in i:
        print(j,end=" ")
    print()