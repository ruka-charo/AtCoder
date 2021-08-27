# 変数
n = int(input())
a = [input().split() for l in range(n)]


answer = []
for i in range(n):
    # 次の点までの差分
    if i == 0: pass
    else:
        a[i] = [int(j) for j in a[i]]
        a[i-1] = [int(j) for j in a[i-1]]

        a[i][0] -= a[i-1][0]
        a[i][1] -= a[i-1][1]
        a[i][2] -= a[i-1][2]

    a[i] = [int(j) for j in a[i]]
    num = a[i][0] - (abs(a[i][1]) + abs(a[i][2]))

    # 到達可能条件
    if 0 <= num and num % 2 == 0:
        answer.append('Yes')
    else:
        answer.append('No')

# 最終的な答え
if 'No' not in answer:
    print('Yes')
else:
    print('No')
