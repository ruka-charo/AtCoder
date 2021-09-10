n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
mod = 1e9 + 7

dice_avg = []
# 各サイコロの出目の期待値
for dice in a:
    dice_avg.append(sum(dice))

s = 1
for point in dice_avg:
    s = (s*point) % mod

print(s)
