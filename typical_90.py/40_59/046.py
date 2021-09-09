import collections
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))


# リスト内の要素を46で割っておく
a = [i%46 for i in a]
a_set = set(a)
b = [i%46 for i in b]
b_set = set(b)
c = [i%46 for i in c]
c_set = set(c)

a_count = collections.Counter(a)
b_count = collections.Counter(b)
c_count = collections.Counter(c)

counts = 0
for i in a_set:
    for j in b_set:
        for k in c_set:
            if (i + j + k) % 46 == 0:
                counts += a_count[i] * b_count[j] * c_count[k]

print(counts)
