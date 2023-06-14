n = int(input())
while n > 0:
    a,b = map(int,input().split())
    m = list(map(int,input().split()))
    m1 = m[b:len(m)]
    m2 = m[0:b]
    for i in m1:
        print(i,end=' ')
    for i in m2:
        print(i,end=' ')
    print()
    n -=1
