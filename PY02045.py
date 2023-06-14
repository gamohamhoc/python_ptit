a = str(input())
while len(a)>1:
    x=int(len(a)/2)
    y=a[0:x]
    z=a[x:len(a)]
    s=int(y)+int(z)
    print(s)
    a=str(s)