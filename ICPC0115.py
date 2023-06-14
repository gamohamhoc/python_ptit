m=[]
m.append(1)
tich=1
for i in range(1,10):
    tich *= i
    m.append(tich)
n = int(input())
while n > 0:
    tong =0
    a = int(input())
    x=a
    while x > 0:
        tong += m[x%10]
        x = int(x/10)
    print(tong)
    if tong == a: print("Yes")
    else: print("No")
    n -=1