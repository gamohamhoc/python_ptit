a,b = map(str,input().lower().split('.'))
if len(a)+len(b)>3 and b=='py':
    print("yes")
else:
    print("no")