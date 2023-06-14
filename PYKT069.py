class student:
    def __init__(self, name , AC , submit):
        self.name=name
        self.AC=AC
        self.submit=submit
ds=[]
n = int(input())
while n>0:
    name=input()
    a,b=map(int,input().split())
    ds.append(student(name,a,b))
    n -=1
ds=sorted(ds,key=lambda x:(x.AC,x.submit,x.name))
for i in ds:
    print("{} {} {}".format(i.name,i.AC,i.submit))
