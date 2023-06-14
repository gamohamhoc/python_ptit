def check(s):
    for i in range(0,int((len(s)+1)/2)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True
file = open('VANBAN.in','r')
dict={}
Max=0
for x in file:
    if x[-1]==' ' or x[-1]=='\n':
        x = x[:-1]
    ds=list(map(str,x.split(' ')))
    for i in ds:
        if check(i):
            if Max <= len(i):
                Max = len(i)
                if i in dict:
                    dict[i] +=1
                else:
                    dict[i] = 1
file.close()
for i in dict:
    if len(i)==Max:
        print(i,dict[i])
    

