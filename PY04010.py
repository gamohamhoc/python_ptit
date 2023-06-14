import math
class TS:
    def __init__(self,name,date,p1,p2,p3):
        self.name = name
        self.date = date
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def tong(self):
        return self.p1+self.p2+self.p3
    def hien(self):
        tong=self.p1+self.p2+self.p3
        return "{} {} {:.1f}".format((self.name).title(),self.date,tong)
ds=[]
for i in range(5):
    ds.append(str(input()))
ts1=TS(ds[0],ds[1],float(ds[2]),float(ds[3]),float(ds[4]))
print(ts1.hien())