import itertools
s =str(input())
ds=itertools.permutations(s)
for i in ds:
    for j in i:
        print(j,end="")
    print()