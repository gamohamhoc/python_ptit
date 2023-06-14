def check(a):
    if len(a)<2: return False
    if a!=a[::-1]: return False
    return True
a,b=map(int,input().split())
ds=[]
for i in range(a):
    ds.append(list(map(int,input().split())))
Max=0
ktra=0
for i in ds:
    for j in i:
        if check(str(j)):
            Max=max(Max,j)
            ktra=1
dem=0
if ktra==0:
    print("NOT FOUND")
else:
    print(Max)
    for i in ds:
        dem1=0
        for j in i:
            if j==Max:
                print("Vi tri ["+str(dem)+"]["+str(dem1)+"]")
            dem1 +=1
        dem +=1