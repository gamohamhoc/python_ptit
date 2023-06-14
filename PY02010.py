while 1:
    a = int(input())
    if int(a)==0:
        break
    else:
        ds=[]
        for i in range(a):
            x = str(input())
            ds.append(int(x))
        if min(ds) != max(ds):
            print(min(ds),max(ds))
        else:
            print("BANG NHAU")