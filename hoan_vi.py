check =[0]*10000
n=4
a=[1,3,4,5]
x=[0]*10000
def Try(i):
    for j in range(1,n+1):
        if(check[j]==0):
            x[i]=j
            check[j]=1
            if i==n:
                for k in range(1, n+1):
                    print(a[x[k]-1],end=' ')
                print()
            else: Try(i+1)
            check[j]=0
Try(1)