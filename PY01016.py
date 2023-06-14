n = int(input());
while n > 0:
    val = str(input());
    i = 0;
    x = int(len(val));
    while i < x - 1:
        dem = int(val[i+1])
        while dem > 0 :
            print(val[i], end = '')
            dem -= 1
        i += 2
    n -= 1
    print()