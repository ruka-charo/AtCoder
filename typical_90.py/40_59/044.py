n, q = map(int, input().split())
a = list(map(int, input().split()))
txy = [map(int, input().split()) for _ in range(q)]
t, x, y = map(list, zip(*txy))

for i in range(q):
    if t[i] == 1:
        a[x[i]-1], a[y[i]-1] = a[y[i]-1], a[x[i]-1]

    elif t[i] == 2:
        a = [a[n-1]] + a[:n-1]

    else:
        print(a[x[i]-1])
