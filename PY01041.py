n = int(input())
def check1(x):
    if len(x)>2: return True
    return False
def check2(x):
    i=0
    while i < len(x) -1:
        if x[i] >= x[i+1]:
            return i
        i +=1
def check3(x):
    i=len(x)-1
    while i >0:
        if x[i] >= x[i-1]:
            return i
        i -=1
while n > 0:
    x = str(input())
    if(check2(x)==check3(x) and check1(x)): print("YES")
    else: print("NO")
    n -=1