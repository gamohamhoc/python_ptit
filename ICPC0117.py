n = int(input())
a1 =[]
while n > 0:
    val = str(input())
    a1.append(val)
    n -=1
a2 = set(a1)
print(len(a2))