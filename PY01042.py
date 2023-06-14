def check(a):
    for i in a:
        if (i!='0' and i !='1' and i !='2'): return 1
    return 0
n = int(input())
while ( n > 0):
    a = str(input())
    if check(a)==1: print("NO")
    else: print("YES")
    n -=1