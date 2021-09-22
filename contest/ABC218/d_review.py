from itertools import combinations
from bisect import bisect_left
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]


# 対角線に沿った座標を全探索
all_list = list(combinations(xy, 2))


# 残りの2つの座標を見つける関数
def find_coor(xy_list):
    xy_list1 = [xy_list[0][0], xy_list[1][1]]
    xy_list2 = [xy_list[1][0], xy_list[0][1]]

    return xy_list1, xy_list2


# 全探索から4つの座標を算出
counts = 0
for xy_list in all_list:
    rest_list = find_coor(xy_list)
    index = bisect_left(all_list, rest_list)

    judge = False
    if index == 0:
        if (all_list[index] == rest_list):
            judge = True
            
    elif index == len(all_list):
        if (all_list[index-1] == rest_list):
            judge = True

    else:
        if (all_list[index] == rest_list) or (all_list[index-1] == rest_list):
            judge = True

    if judge:
        counts += 1

print(counts)

all_list
