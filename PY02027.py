a = int(input())
ds=[]
for i in range(a):
    x = str(input())
    if x[-1]=='\n':
        x = x[:-1]
    z=0
    hien =""
    while z<len(x):
        t=x[z]
        if t.isdigit():
            hien=""
            while z<len(x) and t.isdigit():
                hien= hien + t
                z +=1
                if z ==len(x):
                    break
                t = x[z]
            ds.append(int(hien))
        else:
            z +=1
ds=sorted(ds)
for i in ds:
    print(i)