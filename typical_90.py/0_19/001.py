# miss ==========================================================
import bisect

x = list(map(int, input().split()))
n, l = x[0], x[1]
k = int(input())
a = list(map(int, input().split()))


# k+1個に分ける時の平均の切れ目
a_avg = l / (k+1)
a_best = [a_avg*(i+1) for i in range(k)] # ベストな切れ目のリスト


# 平均の切れ込みから最も近い切れ込みをk個探す
piece = [0] # 選ぶ切り込み
for p in a_best:
    index = bisect.bisect_left(a, p)
    if index == 0:
        piece.append(a[0])
    else:
        if (a[index] - p) < (p - a[index-1]):
            piece.append(a[index])
        elif (a[index] - p) > (p - a[index-1]):
            piece.append(a[index-1])
        else:
            if l/2 > p:
                piece.append(a[index])
            else:
                piece.append(a[index-1])

piece.insert(len(piece), l)


# 切れ込みからピースの大きさを計算
piece_size = [piece[i]-piece[i-1] for i in range(1, len(piece))]
print(min(piece_size))


#%% corr =========================================================
x = list(map(int, input().split()))
n, l = x[0], x[1]
k = int(input())
a = list(map(int, input().split()))


def boarder(r):
    counts = 0 # カットの回数
    pre = 0 # 前回の切れ目

    for i in range(n):
        length = a[i]
        if length - pre >= r and l - length >= r: # 最後の要素の調整あり
            counts += 1
            pre = length

    if counts >= k:
        return True
    else:
        return False


left = 0
right = l

while right - left > 1:
    r = (left + right) // 2
    if boarder(r):
        left = r
    else:
        right = r

print(left)
