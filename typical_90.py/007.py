import bisect

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]

a = sorted(a)

for i in range(q):
    index = bisect.bisect_right(a, b[i])
    if index == 0:
        score_1 = abs(b[i] - a[index])
        print(score_1)
    elif index > n - 1:
        score_2 = abs(b[i] - a[index-1])
        print(score_2)
    else:
        score_1 = abs(b[i] - a[index])
        score_2 = abs(b[i] - a[index-1])
        print(min(score_1, score_2))
