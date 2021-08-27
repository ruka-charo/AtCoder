# 整数の入力
a = int(input())
# スペース区切りの整数の入力
b = list(map(int, input().split()))

def f(c):
    return c/2

cnt = 0
while all(i%2==0 for i in b):
    b = [j for j in map(f, b)]
    cnt += 1

print(cnt)
