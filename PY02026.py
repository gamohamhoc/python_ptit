def check(dict1,dict2):
    if len(dict1)!=len(dict2):
        return False
    for i in dict1:
        if i not in dict2:
            return False
    return True
a,b=map(int,input().split())
ds1=list(map(int,input().split()))
ds2=list(map(int,input().split()))
ds1=sorted(ds1)
ds2=sorted(ds2)
dict1={}
dict2={}
for i in ds1:
    dict1[i]=1
for i in ds2:
    dict2[i]=1
if check(dict1,dict2):
    print("YES")
else: print("NO")
