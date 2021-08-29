# 15分

n = int(input())
a = [input().split() for l in range(n)]



answer = []
for name in a:
    if a.count(name) >= 2:
        answer.append('Yes')
    else:
        answer.append('No')

if 'Yes' in answer:
    print('Yes')
else:
    print('No')
