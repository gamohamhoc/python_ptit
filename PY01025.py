val = str(input())
x = int(len(val))
y = x % 3
for i in range(0,y):
    print(val[i],end='')
if y>0 and len(val)> 3 :
    print(",",end='')
dem=1
for i in range(y,x):
    print(val[i],end='')
    if dem == 3: 
        if i!=x-1: print(",",end='')
        dem=0
    dem +=1
print()