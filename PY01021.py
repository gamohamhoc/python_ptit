n = int(input())
while n >0:
    kq =""
    tong =0
    s = str(input())
    for i in range(0,len(s)):
        if s[i].isalpha():
            kq +=s[i]
        if s[i].isdigit():
            tong += int(s[i])
    kq = sorted(kq)
    for i in kq:
        print(i,end="")
    print(tong)
    n -=1