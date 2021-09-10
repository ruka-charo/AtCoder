from itertools import combinations
n, p, q = map(int, input().split())
a = list(map(int, input().split()))


counts = 0
for s, t, u, v, w in combinations(a, 5):
    if s%p * t%p * u%p * v%p * w%p == q:
        counts += 1

print(counts)
