n = int(input())
import math
def check10(a):
    dem=0
    for i in range(0,len(a)):
        dem += ord(a[i]) - ord('0')
    if dem % 10 == 0: return 1
    return 0
def check(a):
    for i in range(1,len(a)):
        if abs(ord(a[i])-ord(a[i-1])) != 2 :
            return 0
    return 1
while n > 0:
    val = str(input())
    if check10(val) == 1 and check(val) == 1:
        print("YES")
    else: print("NO")
    n -= 1
