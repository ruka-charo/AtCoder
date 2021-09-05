# 75分
n = int(input())
p = list(map(int, input().split()))


q = []
p_dict = {}
for i in range(n):
    p_dict[p[i]] = i+1

for j in range(n):
    q.append(p_dict[j+1])

print(*q)
