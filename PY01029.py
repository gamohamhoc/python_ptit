n = int(input())
def ucln(a,b):
    if b ==0: return a
    else: return ucln(b,a%b)
while n > 0:
    x = int(input())
    y =x
    z=0
    while y > 0:
        z = z*10 + y%10
        y = int(y/10)
    if ucln(x,z) == 1: print("YES")
    else: print("NO")
    n -=1
