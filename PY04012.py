class cc:
    def __init__(self,msv,name,lop,):
        self.msv=msv
        self.name=name
        self.lop=lop
    def setDiem(self,Diemcc):
        self.Diemcc=Diemcc
    def xeploai(self,Diemcc):
        if self.Diemcc==0:
            return 'KDDK'
        return ''
    def __str__(self):
        return self.msv+ " "+self.name+" "+self.lop+" "+str(self.Diemcc)+" "+self.xeploai(Diemcc)
def Diemcc(s):
    v = s.count('v')
    m = s.count('m')
    diem=10-2*v-m
    if diem<0: return 0
    return diem
n = int(input())
ds=[]
for i in range(n):
    msv=str(input())
    name =str(input())
    lop=str(input())
    ds.append(cc(msv,name,lop))
for i in range(n):
    a=[x for x in input().split()]
    tmp = Diemcc(a[1])
    for j in ds:
        if a[0]==j.msv:
            j.setDiem(tmp)
for i in ds:
    print(i)