class Rectangle:
    def __init__(self,d,r,m):
        self.d=d
        self.r=r
        self.m=m
    def area(self):
        return self.d*self.r
    def perimeter(self):
        return 2*(self.d+self.r)
    def color(self):
        return self.m.title()

arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), (arr[2]))
if (int(arr[0]) > 0) and (int(arr[1]) > 0):
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")
