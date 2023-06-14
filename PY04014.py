import math
class student:
    def __init__(self,stt,name,mark):
        self.stt=stt
        self.name=name
        self.mark=mark
    def xeploai(self):
        if self.mark >= 9.0:
            return 'XUAT SAC'
        elif self.mark >= 8.0:
            return 'GIOI'
        elif self.mark >= 7.0:
            return 'KHA'
        elif self.mark >= 5.0:
            return 'TB'
        else:
            return 'YEU'
    def lamtron(self,mark):
        mark = (mark *100+1)/100
        return round(mark,1)
    def __str__(self):
        return self.stt+" "+self.name+" "+str(self.lamtron(self.mark))+" "+self.xeploai()
def cmp(a):
    return (a.mark,(-1)*a.stt)
ds=[]
n = int(input())
for i in range(1,n+1):
    stt="HS"
    if i<10:
        stt = stt +"0"+str(i)
    else:
        stt=stt+str(i)
    name= str(input())
    tong=0
    ds1=list(map(float,input().split()))
    ds1[0] *=2
    ds1[1] *=2
    for i in ds1:
        tong +=i
    tong = (tong)/12
    ds.append(student(stt,name,tong))
ds.sort(key=cmp,reverse=True)
for i in ds:
    print(i)

