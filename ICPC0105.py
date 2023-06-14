n= int(input())
while n > 0:
    val = str(input())
    x =0
    hien=[]
    so =""
    for i in range(0,len(val)):
        if val[i] >='0' and val[i] <='9':
            so += val[i]
        else:
            if so != "":
                hien.append(int(so))
                so =""
    if so != "":
        hien.append(int(so))
        so =""
    m = -1e18
    for i in hien:
        if i > m:
            m=i
    print(m)
    n -=1
