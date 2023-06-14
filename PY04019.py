import math
class nv:
    def __init__(self,stt,name,tb):
        self.stt=stt
        self.name=name.title()
        self.tb=round(tb,2)
    def loai(selfs,tb):
        if tb<5:
            return 'TRUOT'
        if tb<8:
            return 'CAN NHAC'
        if tb<9.5:
            return 'DAT'
        return 'XUAT SAC'
    def __str__(self):
        return '{} {} {:.2f} {}'.format(self.stt,self.name,self.tb,self.loai(self.tb))
def cmp(a):
    return a.tb
ds=[]
for i in range(1,int(input())+1):
    stt="TS"
    # if i<10:
    #     stt =stt+"0"+str(i)
    # else:
    stt = stt+"0"+str(i)
    name=str(input())
    a=float(input())
    if a>10:
        a=a/10
    b=float(input())
    if b>10:
        b=b/10
    tb=(a+b)/2
    ds.append(nv(stt,name,tb))
ds.sort(key=cmp,reverse=True)
for i in ds:
    print(i)

