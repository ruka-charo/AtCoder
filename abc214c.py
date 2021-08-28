# 変数
n = int(input()) # 人数
a = [input().split() for l in range(2)]
s = a[0] # 隣に渡す時間
t = a[1] # 高橋くんが渡す時間

# sとtの各要素をint型に直す
s = [int(i) for i in s]
t = [int(i) for i in t]
u = [i+j for i, j in zip(s, t)] # s+tのリスト


time = [[] for i in range(n)]

# すぬけ君から渡される時間の候補
for i in range(n): # i番目のすぬけ君に対し
    for j in range(n-1): # 候補を格納
        if j == 0:
            time[i].append(u[i-j-1])
        else:
            sum_s = sum([s[k] for k in range(i-j, n-1)])
            if min(time[i]) > (u[i-j-1] + sum_s):
                time[i].append(u[i-j-1] + sum_s)
            else: continue

# 高橋君から渡られる時間を追加
for i in range(n):
    if min(time[i]) > t[i]:
        time[i].append(t[i])
    else: continue


# それぞれの時間の最小値を求める
for time_min in [min(i) for i in time]:
    print(time_min)


# アルゴリズムを変えないと時間超過してしまう…。
