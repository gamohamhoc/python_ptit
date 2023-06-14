n = float(input())
x = float(100)
while n > 0 :
    a,b,c = map(float,input().split())
    dem = int(0)
    while a <= c :
        a = a *  (1 + b / x)
        dem = dem + 1
    print(int(dem))
    n = n - 1 ;