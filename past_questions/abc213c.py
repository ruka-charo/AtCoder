x = list(map(int, input().split()))
h, w, n = x[0], x[1], x[2]

ab = [map(int, input().split()) for _ in range(n)]
a, b = map(list, zip(*ab))


rank_a = {num: i+1 for i, num in enumerate(sorted(set(a)))}
rank_b = {num: i+1 for i, num in enumerate(sorted(set(b)))}


for i, j in zip(a, b):
    print(rank_a[i], rank_b[j])
