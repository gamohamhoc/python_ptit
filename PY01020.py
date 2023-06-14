n = int(input());
while n > 0:
    val = str(input());
    x = int(len(val));
    if val[x-1] =='6' and val[x-2] =='8' :
        print("YES");
    else: print("NO");
    n = n - 1 ;