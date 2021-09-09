n, q = map(int, input().split())
a = list(map(int, input().split()))
txy = [map(int, input().split()) for _ in range(q)]
t, x, y = map(list, zip(*txy))


shift = 0
for i in range(q):
    if t[i] == 1:
        a[(x[i]-1-shift)%n], a[(y[i]-1-shift)%n] = \
        a[(y[i]-1-shift)%n], a[(x[i]-1-shift)%n]

    elif t[i] == 2:
        shift += 1

    else:
        print(a[(x[i]-1-shift)%n])
