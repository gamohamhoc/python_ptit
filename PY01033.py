a,b = map(int,input().split())
import math
for x in range(a,b+1):
    for y in range(x+1,b+1):
        for z in range(y+1,b+1):
            if math.gcd(x,y) == 1 and math.gcd(x,z) == 1 and math.gcd(z,y) == 1:
                print("(",end='')
                print(x,end=', ')
                print(y,end=', ')
                print(z,end=')')
                print()