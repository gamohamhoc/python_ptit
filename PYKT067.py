n = int(input())
import itertools
while n > 0:
    a= int(input())
    ds=[]
    for i in range(-a,0):
        ds.append(-i)
    x = list(itertools.permutations(ds))
    print(len(x))
    for i in x:
        for j in i:
            print(j,end="")
        print(end=" ")
    print()
    n -=1