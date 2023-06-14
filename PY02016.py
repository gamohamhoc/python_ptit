n = int(input())
while n > 0:
    a = int(input())
    ds = list(map(int, input().split()))
    dic ={}
    for i in ds:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] =1
    Max = max(dic.values())
    if Max > a/2:
        for i in ds:
            if dic[i]==Max:
                print(i)
                break
    else: print("NO")
    n -=1