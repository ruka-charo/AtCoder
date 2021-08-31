import bisect

x = list(map(int, input().split()))
n, m = x[0], x[1]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b)


min_num = 1e9
for i in a:
    index = bisect.bisect_right(b, i)
    if index == 0:
        c = abs(i - b[index])
        if min_num > c:
            min_num = c

    elif index == m:
        index = bisect.bisect_left(b, i)
        c = abs(i - b[index-1])
        if min_num > c:
            min_num = c

    else:
        c = abs(i - b[index])
        d = abs(i - b[index - 1])
        e = min(c, d)
        if min_num > e:
            min_num = e

print(min_num)
