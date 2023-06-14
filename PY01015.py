n = int(input())
while n > 0:
    val = str(input())
    check = int(0);
    for i in range(int(len(val))-2) :
        if val[i] > val[i+1] :
            check = 1;
    if(check == 0): print("YES");
    else: print("NO");
    n = n - 1
    
