n = int(input())
while n > 0:
    val = str(input())
    val2 = list(val)
    val2.reverse()
    val3 = ''.join(val2)
    x = int(len(val))
    check = 1
    for i in range(1, x-1) :
        if(abs( ord(val[i]) - ord(val[i-1])) != abs(ord(val2[i]) - ord(val2[i-1]))):
            check = 0
    if(check == 0) : print("NO")
    else: print("YES")        
    n -= 1