import re

n =  int(input())
dict={}
while n>0:
    s=str(input())
    s=s.lower()
    dau=" ,.?!:;()-/"
    tach_dau = '|'.join(map(re.escape,dau))
    ds=re.split(tach_dau,s)
    for i in ds:
        if i not in dict:
            dict[i]=1
        else:
            dict[i] +=1
    n -=1
m = sorted(dict.items(),key=lambda x: ((-1)*x[1],1*x[0]))
for i in m:
    if i[0]!='':
        print("{} {}".format(i[0],i[1]))