# 初見(もれあり) ================================================================

n = int(input())

# 奇数(indexは偶数)の時は正しい括弧列は作れない
if n % 2 == 1:
    print('')
else:
    # 格納用リストと初期値
    a = [[] for i in range(n)]
    a[1].append('()')

    for i in range(2, n):
        if 2*i > n:
            continue
        else:
            a[2*i-1].append('('+ a[2*i-3][0] +')')
            for j in range(2, n):
                if 2*i-2*j+1 < 0:
                    continue
                else:
                    # 全ての組み合わせを試さないといけない
                    for k in range(len(a[2*i-2*j+1])):
                        for l in range(len(a[2*j-3])):
                            a[2*i-1].append(a[2*i-2*j+1][k] + a[2*j-3][l])
                            a[2*i-1].append(a[2*j-3][l] + a[2*i-2*j+1][k])


    a_set = list(set(a[n-1])) # 重複を除く

    # 括弧を数字に直して辞書順に並べられるようにする
    for i, ele in enumerate(a_set):
        a_set[i] = ele.replace('(', '1').replace(')', '2')

    # 辞書順に並べてから元に戻す
    a_sorted = sorted([int(num) for num in a_set])
    a_sorted = [str(word) for word in a_sorted]

    for i, ele in enumerate(a_sorted):
        a_sorted[i] = ele.replace('1', '(').replace('2', ')')

    # 答えを出力
    for ans in a_sorted:
        print(ans)

#%% ans =======================================================================
from itertools import product

n = int(input())

# bit全探索
bit_list = list(product([0, 1], repeat=n))


def judge(bit_list):
    counts = 0
    for num_list in bit_list:
        for num in num_list:
            if num == 0:
                counts -= 1
                if counts < 0:
                    print(False)
            else:
                counts += 1




judge(bit_list)
