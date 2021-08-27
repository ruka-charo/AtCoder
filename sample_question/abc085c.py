# 変数
x = list(map(int, input().split()))
n, y = x[0], x[1]


money_num = []
# 解を全数探索
for p in range(n+1):
    if len(money_num) >= 1:
        break
    for q in range(n+1):
        price = 9000*p + 4000*q + 1000*n
        if price == y and n-p-q >= 0:
            money_num.append([p, q, n-p-q])

# 解がなかった場合
if len(money_num) == 0:
    money_num.append([-1, -1, -1])

print(*money_num[0])
