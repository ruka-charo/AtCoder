p = list(map(int, input().split()))
a = list(map(int, input().split()))
n, x = p[0], p[1]

price = 0
for i in range(n):
    if (i+1)%2 == 0:
        price += a[i] - 1
    else:
        price += a[i]

if x >= price:
    print('Yes')
else:
    print('No')
