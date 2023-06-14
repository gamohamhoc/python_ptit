a,b=map(int,input().split())
ds1=list(map(int,input().split()))
dict1={}
for i in ds1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1
m=sorted(dict1.items(),key=lambda x:(x[1],x[0]))
Max=0
Min=10000000000000
for i in m:
    Max =max(Max,i[1])
    Min = min(Min,i[1])
if Max==Min:
    print("NONE")
else:
    for i in range(len(m)-1,-1,-1):
        if m[i][1] != Max:
            print(m[i][0])
            break
