def check(tong):
    if tong < 10:
        return False
    s = str(tong)
    for i in range(0,int((len(s)+1)/2)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True
n = int(input())
while(n > 0):
    s = str(input())
    tong =0
    for i in range(0, len(s)):
        tong = tong + int(s[i])
    if check(tong):
        print("YES")
    else: print("NO")
    n -=1