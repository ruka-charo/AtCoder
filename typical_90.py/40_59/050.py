n, l = map(int, input().split())
mod = 1e9 + 7

# 初項の設定(0段目を含む)
a = [1 if i<l else 0 for i in range(n+1)]


for i in range(l, n+1):
    a[i] = (a[i-1] + a[i-l])%mod

print(int(a[-1]))
