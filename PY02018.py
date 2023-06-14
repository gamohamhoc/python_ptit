n = input()
ds = list(map(int, input().split()))
print(min(i for i in range(1,max(ds)+2) if i not in ds))