n = int(input())
while n > 0:
    a = int(input())
    ds = list(map(str,input().split()))
    ds2 =[]
    for i in ds:
        tong =0
        for j in i:
            tong += int(j)
        ds2.append(tong)
    for i in range(0,len(ds2)-1):
        for j in range(i+1,len(ds2)):
            if ds2[i]> ds2[j]:
                c=ds2[i]
                ds2[i]=ds2[j]
                ds2[j]=c
                c=ds[i]
                ds[i]=ds[j]
                ds[j]=c
    for i in range(0,len(ds2)-1):
        j =i+1
        while j<len(ds2) and ds2[i]==ds2[j]:
            if int(ds[i])> int(ds[j]):
                c=ds[i]
                ds[i]=ds[j]
                ds[j]=c
            j +=1
    for i in ds:
        print(i,end=" ")
    print()
    n -=1