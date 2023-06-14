import math
class Ps:
    def __init__(self,t,m):
        self.t=t
        self.m=m
    def rut_gon(self):
        a=math.gcd(self.t,self.m)
        self.t //=a
        self.m //=a
        return self
    def tong(a,b):
        mau = a.m*b.m // math.gcd(a.m,b.m)
        ps = Ps(a.t*mau // a.m + b.t*mau // b.m,mau)
        return ps.rut_gon()
a,b,c,d = map(int,input().split())
A=Ps(a,b)
B=Ps(c,d)
C = A.tong(B)
print(str(C.t)+"/"+str(C.m))