import math
class Ps:
    def __init__(self,t,m):
        self.t=t
        self.m=m
    def kq(self):
        a=math.gcd(self.t,self.m)
        self.t /= a
        self.m /= a
        return "{:.0f}/{:.0f}".format(self.t,self.m)
tu, mau = map(int,input().split())
A =Ps(tu,mau)
print(A.kq())