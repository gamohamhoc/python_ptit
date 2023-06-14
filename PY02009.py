n = int(input())
while n > 0:
    a = int(input())
    ds =[] # list
    dic ={} # từ điển
    Max=0
    for i in range(0,a):
        x = int(input())
        if x in dic:
            dic[x] +=1
        else:
            ds.append(x)
            dic[x]=1
    for i in ds:
        print(dic[i],end=" ")
    n -=1
    print("")