from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))


a_2 = a + a
total = sum(a) # ホールケーキの大きさ

if total % 10 != 0:
    exit(print('No'))

num = total // 10

# 前からの累積和、後ろからの累積和
x, y = [a[0]], [a[-1]]
for i in range(n-1):
    x.append(a[i+1] + x[-1])
    y.append(a[-2-i] + y[-1])

for i in range(n):
    # 目的の大きさと一致した場合
    if x[i] == num:
        exit(print('Yes'))

    # 目的の大きさよりも多く選んでしまった場合
    elif x[i] > num:
        j = bisect_left(x, x[i]-num)
        if x[i] - x[j] == num:
            exit(print('Yes'))

    # 目的の大きさより小さい場合は後ろから持ってくる
    elif x[i] < num:
        j = bisect_left(y, num - x[i])
        if x[i] + y[j] == num:
            exit(print('Yes'))

print('No')
