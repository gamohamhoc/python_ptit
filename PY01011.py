n = int(input())
ds =["0","2","4","6","8"]
while( n > 0):
    a = int(input())
    for i in range(0,a):
        tmp = str(i);
        if len(tmp) %2 !=0 or "".join(list(reversed(tmp))) != tmp:
            continue
        else:
            check =1
            for j in tmp:
                if j not in ds:
                    check =0
                    break
            if check ==0:
                continue
            else: print(i,end =" ")
    print()
    n -=1