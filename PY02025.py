a,b = map(int,input().split())
ds1=list(map(int,input().split()))

ds2=list(map(int,input().split()))
dict1={}
dict2={}
ds1=sorted(ds1)
ds2=sorted(ds2)
for i in ds1:
    dict1[i] =1
for i in ds2:
    dict2[i] =1

for i in dict1:
    if i in dict2:
        print(i,end=" ")
print()
for i in dict1:
    if i not in dict2:
        print(i,end=" ")
print()
for i in dict2:
    if i not in dict1:
        print(i,end=" ")