n = int(input());
while n > 0 :
    x = input();
    val = str(input());
    check = int(1);
    for i in val :
        if i != '4' and i != '7':
            check = 0;
    if(check == 1) : 
        print("YES");
    else: print("NO");
    n = n - 1;
