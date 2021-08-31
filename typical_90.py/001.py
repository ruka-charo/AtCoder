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
