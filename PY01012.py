s1=str(input())
s2=str(input())
n =int(input())
kq=str("")
for i in range(0,n-1):
    kq += s1[i]
kq +=s2
for i in range(n-1,len(s1)):
    kq += s1[i]
print(kq)