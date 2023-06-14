import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(a,b):
        return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)
    def do_dai(p1,p2,p3):
        a=p1.distance(p2)
        b=p2.distance(p3)
        c=p3.distance(p1)
        if (p1.distance(p2)+p2.distance(p3) <=p3.distance(p1)) or (p1.distance(p2)+p1.distance(p3) <=p3.distance(p2)) or (p3.distance(p2)+p1.distance(p3) <=p2.distance(p1)):
            return("INVALID")
        else:
            return("{:.2f}".format(1/4 *math.sqrt((a+b+c)*(a+b-c)*(-a+b+c)*(a-b+c))))
t = int(input())
hien =[]
ds1=[]
while t >0:
    ds1.append(list(map(float,input().split())))
    t -=1
for ds in ds1:
    p1=Point(ds[0],ds[1])
    p2=Point(ds[2],ds[3])
    p3=Point(ds[4],ds[5])
    for i in ds1:
        for j in i:
            if abs(j)>1000:
                hien.append("INVALID")
    hien.append(str(p1.do_dai(p2,p3)))
    t -=1
for i in hien:
    print(i)