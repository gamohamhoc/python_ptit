n = int(input())
while n > 0:
    a = int(input())
    i =2
    print(1,end="")
    while i <=a:
        dem =0
        if a%i==0:
            while a%i==0:
                a /=i
                dem +=1
            hien = str(i)+"^"+str(dem)
            print(" *",hien,end="")
        i +=1
    print()
    n -=1
