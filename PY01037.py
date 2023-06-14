import math
n= int(input())
def uoc(a):
    dem=0
    if a<3: return a
    if math.sqrt(a)==int(math.sqrt(a)) :
        dem-=1
    for i in range(1,int(math.sqrt(a))+1):
        if a%i==0:
            dem +=2
    return dem
while n>0:
    a=int(input())
    x=0
    if a%2==0:
        x -=2
    else:
        x -=1
    while uoc(x)>=uoc(a):
        a +=2
    print(a)
    n -=1