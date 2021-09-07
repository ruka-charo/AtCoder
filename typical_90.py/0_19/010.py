# 2連続forループのせいで制限時間超過 ============================

n = int(input())
cp = [map(int, input().split()) for _ in range(n)]
c, p = map(list, zip(*cp))
q = int(input())
lr = [map(int, input().split()) for _ in range(q)]
l, r = map(list, zip(*lr))



class_1 = 0 # 点数の合計
class_2 = 0 # 点数の合計

for j in range(q):# 質問の回数分繰り返す
    for i in range(l[j], r[j]+1):
        if c[i-1] == 1:
            class_1 += p[i-1]
        else:
            class_2 += p[i-1]

    print(class_1, class_2)

    # 次の質問のために初期化
    class_1, class_2 = 0, 0


# ans ======================================================
# 累積和を用いる
n = int(input())
cp = [map(int, input().split()) for _ in range(n)]
c, p = map(list, zip(*cp))
q = int(input())
lr = [map(int, input().split()) for _ in range(q)]
l, r = map(list, zip(*lr))

# 累積和リスト
sum1_list = []
sum2_list = []

for i in range(n):
    if i == 0:
        if c[i] == 1:
            sum1_list.append(p[i])
            sum2_list.append(0)
        else:
            sum1_list.append(0)
            sum2_list.append(p[i])

    else:
        if c[i] == 1:
            sum1_list.append(p[i] + sum1_list[i-1])
            sum2_list.append(0 + sum2_list[i-1])
        else:
            sum1_list.append(0 + sum1_list[i-1])
            sum2_list.append(p[i] + sum2_list[i-1])


# 答えの出力
for i in range(q):
    if l[i] == 1:
        ans_1 = sum1_list[r[i]-1]
        ans_2 = sum2_list[r[i]-1]
    else:
        ans_1 = sum1_list[r[i]-1] - sum1_list[l[i]-2]
        ans_2 = sum2_list[r[i]-1] - sum2_list[l[i]-2]

    print(ans_1, ans_2)
