n = int(input())
while n > 0:
    x =  int(input())
    tong =0
    dem =2
    if x % 2 == 1:
        for i in range(1, x+1,2):
            tong += 1/i
    else:
        for i in range(2, x+1,2):
            tong += 1/i
    print("{:.6f}".format(tong))
    n -=1