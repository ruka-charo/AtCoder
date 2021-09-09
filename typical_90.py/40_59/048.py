n, k = map(int, input().split())
ab = [map(int, input().split()) for _ in range(n)]
a, b = map(list, zip(*ab))

# 差分
c = [i-j for i, j in zip(a, b)]

# b, cを結合して値の大きい順に取っていく
d = sorted(b + c, reverse=True)


points = 0
for point in d:
    k -= 1
    points += point
    if k == 0:
        break

print(points)
