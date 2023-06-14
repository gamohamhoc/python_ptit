a,b,c = map(int,input().split())
x = int(c/b)
check = 0
for i in range(1,x+1) :
    if i * b - a > 0 :
        print(i * b - a, end =' ') 
        check =1
if check == 0 :
    print(-1)
print()