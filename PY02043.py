n = int(input())
while n>0:
    s = str(input())
    x =str(input())
    y=len(x)
    dem=0
    i=0
    t=""
    while i<=len(s)-y:
        j=i+y
        t=s[i:j]
        if t==x:
            dem +=1
            i=j+1
        else: i+=1
    print(dem)
    n -=1