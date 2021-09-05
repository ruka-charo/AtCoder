q = int(input())
nm = [map(int, input().split()) for _ in range(q)]
n, m = map(list, zip(*nm))


a = []
for i in range(q):
    if n == 1:
        a.append(m[i])
    elif n == 2:
        print(a[0])
        del a[0]
    else:
        a = sorted(a)
