dem =0
a1=[0]*42
s=0
while True:
    a2 = [int(dem) for dem in input().split()]
    dem += len(a2)
    for i in a2:
        a1[i%42] =1
    if dem ==10: break
for i in a1:
    if i > 0: s +=1
print(s)