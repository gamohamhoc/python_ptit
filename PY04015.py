import math
class water:
    def __init__(self,stt,name,used):
        self.stt=stt
        self.name=name
        self.used=used
    def tien(self,used):
        muc1=0
        muc2=0
        muc3=0
        tong=0
        if used>100:
            phi=105/100
        elif used>50:
            phi=103/100
        else: phi=102/100

        if self.used >100:
            muc1= (self.used-100)*200
            self.used =100
        if self.used >50:
            muc2=(self.used-50)*150
            self.used =50
        muc3=self.used *100
        tong = (muc1 + muc2 + muc3)*phi
        tong =int(round(tong))
        return tong
    def __str__(self):
        return self.stt+" "+self.name+" "+str(self.tien(self.used))
def cmp(a):
    return (a.used)
ds=[]
for i in range(int(input())):
    stt="KH"
    if i+1<10: stt +="0"+str(i+1)
    else: stt +=str(i+1)
    name = str(input())
    a= float(input())
    b= float(input())
    used=b-a
    ds.append(water(stt,name,used))
ds.sort(key=cmp,reverse=True)
for i in ds:
    print(i)


