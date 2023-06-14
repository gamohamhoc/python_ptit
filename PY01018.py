P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while 1 :
    val = str(input());
    T = val.split()
    a = T[0]
    x = int(a)
    hien=""
    if x ==0: break
    b = T[1]
    for i in range(0,int(len(b))):
        for j in range(0,28):
            if P[j]==b[i]: break
        hien = P[(j+x)%28]+hien
    print(hien)
        

        

