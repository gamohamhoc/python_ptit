n =int(input())
while n>0:
    a =int(input())   
    if a%7==0:
        print(a)
    else:
        dem=0
        while dem<=1000 and a%7!=0:
            b=(int(str(str(a)[::-1])))
            dem +=1
            a=a+b
        if dem >1000:
            print(-1)
        else: print(a)
    n -=1