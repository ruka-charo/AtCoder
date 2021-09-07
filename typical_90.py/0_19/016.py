n = int(input())
a, b, c = map(int, input().split())


min_piece = 10000
for i in range(10000):
    for j in range(10000):
        p = n - a*i - b*j
        if p >= 0 and (p % c) == 0:
            k = p // c
            if min_piece > (i+j+k):
                min_piece = i+j+k

print(min_piece)
