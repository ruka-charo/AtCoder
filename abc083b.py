# 変数
x = list(map(int, input().split()))
n, a, b= x[0], x[1], x[2]


answers = []
for i in range(1, n+1):
    num = i
    k_5 = i // 10000 # 最高位
    i -= k_5 * 10000
    k_4 = i // 1000
    i -= k_4 * 1000
    k_3 = i // 100
    i -= k_3 * 100
    k_2 = i // 10
    i -= k_2 * 10
    k_1 = i // 1
    total = sum([k_5, k_4, k_3, k_2, k_1])

    if a <= total <= b:
        answers.append(num)
    else:
        continue

print(sum(answers))
