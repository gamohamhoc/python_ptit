n = int(input())
while n > 0:
    a = int(input())
    ds = list(map(int,input().split()))
    st =[]
    ans=[]
    for i in range(a):
        while len(st) > 0 and ds[i] >= ds[st[-1]]:
            st.pop()
        if len(st)==0:
            ans.append(i+1)
        else:
            ans.append(i-st[-1])
        st.append(i)
    for i in ans:
        print(i,end=" ")
    print()
    n -=1