def ucln(a,b):
    if b ==0: return a
    else: return ucln(b,a % b)
a,b =map(int,input().split())
moc =1
while b > 1:
    moc *= 10
    b -=1
dem = 0
for i in range(moc,moc*10):
    if ucln(i,a)== 1:
        print(i,end=' ')
        dem +=1
        if dem == 10:
            print()
            dem =0