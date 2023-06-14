n = int(input())
while n > 0 :
    check = int(1)
    val = str(input())
    x = val[0]
    y = val[1]
    for i in range(2,int(len(val))-1):
        if val[i] != x  and val[i]!= y :
            check =0
        if val[i] != val[i-2] :
            check = 0
    if check == 1: print("YES")
    else: print ("NO")
    n -= 1