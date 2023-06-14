val = str(input());
n = int(len(val));
x = int(0);
for i in val :
    if i >= 'a' and i <= 'z' :
        x = x + 1
if x >= n-x :
    print(val.lower());
else : print(val.upper());
    
