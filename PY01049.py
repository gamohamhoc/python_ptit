import math
def nto(s):
    for i in range(2,int(math.sqrt(s))+1):
        if  s%i==0 : return False
    else: return True
def check2(s):
    dem1 = 0
    dem2 = 0
    for i in range(0,len(s)):
        if s[i] == '2' or s[i] == '3' or s[i]  == '5' or s[i]  == '7':
            dem1 +=1
        else: dem2 +=1
    if dem1 > dem2: return True
    else: return False
n = int(input())
while n > 0:
    s = str(input())
    if nto(len(s)) and check2(s):
        print("YES")
    else:
        print("NO")
    n -=1
    