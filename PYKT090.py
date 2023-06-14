# file = open("CONTACT.in",'a')
# file.write("hello")
# file.close()
file = open("CONTACT.in",'r')
dict ={}
for i in file:
    if i[-1] =='\n':
        i = i[:-1]
    i= i.lower()
    dict[i]=1
file.close()
dict=sorted(dict.keys())
for i in dict:
    print(i)