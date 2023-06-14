n =  int(input())
while n >0:
    a,b,c=map(int,input().split())
    ds1=list(map(int,input().split()))
    ds2=list(map(int,input().split()))
    ds3=list(map(int,input().split()))
    check =1
    ds1= sorted(ds1)
    ds2= sorted(ds2)
    ds3= sorted(ds3)
    x=0
    y=0
    z=0
    while a>x and b>y and c>z:
        if ds1[x]==ds2[y]==ds3[z]:
            print(ds1[x],end=" ")
            x +=1
            y +=1
            z +=1
            check=0
        else:
            Min = min(ds1[x],min(ds2[y],ds3[z]))
            if ds1[x]==Min:
                x +=1
            if ds2[y]==Min:
                y +=1
            if ds3[z]==Min:
                z +=1
    if check==1:
        print("NO")
    print()
    n-=1