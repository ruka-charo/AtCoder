import bisect

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]

a = sorted(a)

for i in range(q):
    index = bisect.bisect_right(a, b[i])
    if index == 0:
        score_1 = abs(b[i] - a[index])
        print(score_1)
    elif index > n - 1:
        score_2 = abs(b[i] - a[index-1])
        print(score_2)
    else:
        score_1 = abs(b[i] - a[index])
        score_2 = abs(b[i] - a[index-1])
        print(min(score_1, score_2))


#%% (別解) 二分探索法を用いる
n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]

a = sorted(a)

left, right = 0, n-1 # インデックスの数値に合わせる

for i in range(q):
    while right - left > 1:
        if a[(left + right)//2] < b[i]:
            left = (left + right)//2

        elif a[(left + right)//2] > b[i]:
            right = (left + right)//2

        else: break

    if a[(left + right)//2] == b[i]:
        print(0)
    elif (left + right)//2 == n-1:
        print(abs(a[(left + right)//2] - b[i]))
    else:
        print(min(abs(a[(left + right)//2] - b[i]),
                abs(a[(left + right + 2)//2] - b[i])))

    left, right = 0, n-1 # 次の質問のために初期値に戻しておく
