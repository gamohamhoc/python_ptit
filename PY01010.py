n = int(input());
while n > 0:
    val = str(input());
    x = int(len(val));
    if ( str(val[0] + val[1] )) == ( str(val[x - 2] + val[x-1] )) :
        print("YES");
    else: print("NO");
    n = n - 1;
