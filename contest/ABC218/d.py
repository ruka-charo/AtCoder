from collections import Counter
n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
x, y = map(list, zip(*xy))


# x座標が同じものが2つ以上あるものだけを抽出
x_index = set()
for i, num in enumerate(x):
    if Counter(x)[num] >= 2:
        x_index.add(i)

# yも同様に
y_index = set()
for i, num in enumerate(y):
    if Counter(y)[num] >= 2:
        y_index.add(i)

# 考えるべき座標
index = list(x_index & y_index)


if len(index) <= 3:
    exit(print(0))
