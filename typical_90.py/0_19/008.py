n = int(input())
s = input()
t = 'atcoder'

# DP(動的計画法)を用いる
a = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

for i in range(len(s)+1):
    a[i][0] = 1

for i in range(n):
    for j in range(len(t)):
        if s[i] == t[j]:
            a[i+1][j+1] = (a[i][j+1] + a[i][j]) % (1e9+7) # ここで割っておかないとミスる
        else:
            a[i+1][j+1] = a[i][j+1]

print(int(a[n][len(t)]))
