
# 変数の定義
a = int(input())
b = int(input())
c = int(input())
x = int(input())

#%%
a, b, c, x = 30, 40, 50, 6000

# 全数探索
answers = []
for p in range(a+1):
    for q in range(b+1):
        for r in range(c+1):
            price = p*500 + q*100 + r*50
            if price == x and p <= a and q <= b and r <= c:
                answers.append([p, q, r])

print(len(answers))




#%% 初見 =============================================
# 硬貨の変換式
p = x // 500
q = (x % 500) // 100
r = ((x % 500) % 100) // 50

answers = []
# 持っている硬貨よりも多い場合の処理
if a < p:
    q += (p - a)*5
    p -= (p - a)
if b < q:
    r += (q - b)*2
    q -= (q - b)
if c < r: pass
else: answers.append([p, q, r])

#%% ベース解から答えを探索
if p != 0:
    while p > 0:
        p -= 1
        q += 5
        if q > b: break
        else: answers.append([p, q, r])


    while q > 0:
        q -= 1
        r += 2
        if r > c: break
        else: answers.append([p, q, r])

else:
    while q > 0:
        q -= 1
        r += 2
        if r > c: break
        else: answers.append([p, q, r])

print(len(answers))
print(answers)
