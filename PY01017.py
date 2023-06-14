n = int(input());
while n > 0 :
    val = str(input())
    i  = 0
    val = val + '@'
    while i < ( len(val) - 1 ) :
        dem = int(1)
        x = int(i + 1)
        while x < len(val) and val[i] == val[x]:
            dem += 1
            x += 1
        print(dem, end='')
        print(val[i], end='')
        i=x
    n -= 1
    print()
