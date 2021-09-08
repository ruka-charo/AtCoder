import itertools
import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
if m == 0:
    pass
else:
    xy = [map(int, input().split()) for _ in range(m)]
    x, y = map(list, zip(*xy))


# 全ての走者と区間の順列
all_runlist = list(itertools.permutations(range(n)))


# 仲の悪い選手の組み合わせ(仲が悪い=True)
bad_com = [[False for _ in range(n)] for _ in range(n)]

for i in range(m):
    bad_com[x[i]-1][y[i]-1] = True
    bad_com[y[i]-1][x[i]-1] = True


min_time = 10001
for runlist in all_runlist:
    judge = False
    time = 0

    for i in range(n-1):
        if bad_com[runlist[i]][runlist[i+1]]:
            judge = True

    if judge == False:
        for i in range(n):
            time += a[runlist[i]][i]

        if min_time > time:
            min_time = time

if min_time ==10001:
    print(-1)
else:
    print(min_time)
