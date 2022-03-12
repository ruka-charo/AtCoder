from sys import stdin


# 変数
n = int(input()) # 人数
a = [list(map(int, stdin.readline().split())) for _ in range(2)]

s = a[0] # 隣に渡す時間
t = a[1] # 高橋くんが渡す時間


for i in range(2*n):
    if (i-1)%n == -1:
        continue
    else:
        t[i%n] = min(t[i%n], s[(i-1)%n] + t[(i-1)%n])


# それぞれの時間の最小値を求める
for min_time in t:
    print(min_time)
