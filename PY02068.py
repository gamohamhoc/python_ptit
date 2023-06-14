n = int(input())
while n >0:
    a,b,c = map(int,input().split())
    matrix=[]
    for i in range(a):
        matrix.append(list(map(int,input().split())))
    matrix2=[]
    dem=0
    for i in range(0,a-c+1):
        tong =[]
        for j in range(0,b-c+1):
            z=0
            for x in range(i,i+c):
                for y in range(j, j+c):
            #         print(x,y)

            # print("*")
                    z += matrix[x][y]
            tong.append(int(z/(c*c)))
            # print(z)
        matrix2.append(tong)
        dem+=1
    for i in range(0,dem):
        for j in range(0,dem):
            print(matrix2[i][j],end=" ")
        print()
    n -=1
    