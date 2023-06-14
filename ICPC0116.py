n = int(input())
while n> 0:
    val = str(input())
    if val[0]==val[-1]: print("YES")
    else: print("NO")
    n-=1