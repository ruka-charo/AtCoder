n, q = map(int, input().split())
a = list(map(int, input().split()))
lrv = [map(int, input().split()) for _ in range(q)]
l, r, v = map(list, zip(*lrv))


# 両端の差分を求める
b = [a[i]-a[i-1] for i in range(1, n)]

# 現状の不便さ
now = sum(abs(i) for i in b)

# 差分が変化したところだけ更新する
for i in range(q):
    if l[i] > 1:
        now -= abs(b[l[i]-2])
        b[l[i]-2] += v[i]
        now += abs(b[l[i]-2])

    if r[i] < n:
        now -= abs(b[r[i]-1])
        b[r[i]-1] -= v[i]
        now += abs(b[r[i]-1])

    print(now)
