import itertools
ds = ["A","B","C"]
ans =[]
n = int(input())
for i in range(3,n+1):
    ans += list(itertools.product(ds,repeat=i)) 
    # product là hàm kết hợp từng phần từ của ds theo kiểu tổ hợp , repeat là số lần lặp vô hạn đó hay như đoạn trên là chiều dài của tổ hợp
for i in ans:
    if "A" in i and "B" in i and "C" in i:
        if i.count("A") <= i.count("B") and i.count("B") <= i.count("C") :
            print("".join(i))