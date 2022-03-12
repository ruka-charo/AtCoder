S = input()
tar = "chokudai"
mod = 10**9 + 7

dp = [[0 for _ in range(len(tar)+1)] for _ in range(len(S)+1)]

# 動的計画法を使う dp[0][j]は一行前で実装済み
for i in range(len(S)):
    dp[i][0] = 1

for i in range(len(S)):
    for j in range(len(tar)):
        if S[i] != tar[j]:
            dp[i+1][j+1] = dp[i][j+1]
        else:
            dp[i+1][j+1] = dp[i][j+1] + dp[i][j]

print(dp[len(S)][8] % mod)
