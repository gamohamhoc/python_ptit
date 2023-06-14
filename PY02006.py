n = int(input())
while n > 0:
    check =0
    a = int(input())
    a1 = [int(x) for x in input().split()]
    a1.sort()
    a2 = [int(x) for x in input().split()]
    a2.sort()
    for i in range(0,a):
        if a1[i] > a2[i]:
            check =1
    if check ==1: print("NO")
    else: print("YES")
    n -=1