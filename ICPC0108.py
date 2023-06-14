n = int(input())
while n > 0:
    a = int(input())
    m = list(map(int, input().split()))
    m.sort()
    dem=0
    for i in range(0,a-2):
        l = i+1
        r = a-1
        x = m[i]
        while l<r:
            if x + m[l] + m[r] == 0:
                dem +=1
                l +=1
            elif x + m[l] + m[r] <0:
                l +=1
            else:
                r -=1
    print(dem)
    n -=1