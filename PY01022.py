x = input()
dem=0
if len(x)==1: print(1)
else:
    while len(x)!=1:
        tong =0
        for i in x:
            tong += ord(i)-ord('0')
        dem +=1
        x = str(tong)
    print(dem)