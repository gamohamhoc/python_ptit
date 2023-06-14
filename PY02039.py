n = int(input())
matrix =[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
a = int(input())
s1 = s2 = hieu =0
for i in range(0,n-1):
    for j in range(i+1,n):
        s1 += matrix[i][j]
        s2 += matrix[j][i]
if abs(s2-s1)<=a:
    print("YES")
else: print("NO")
print(abs(s2-s1))