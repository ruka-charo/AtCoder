n = int(input())
s = [input() for _ in range(n)]


name_list = set()
for i in range(n):
    if s[i] not in name_list:
        name_list.add(s[i])
        print(i+1)

# setは x in s の計算量が O(1)
