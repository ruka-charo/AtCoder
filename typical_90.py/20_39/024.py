n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


counts = 0
for i in range(n):
    if a[i] == b[i]:
        continue
    else:
        while a[i] != b[i]:
            if a[i] < b[i]:
                a[i] += 1
                counts += 1
            elif a[i] > b[i]:
                a[i] -= 1
                counts += 1

if (k - counts) > 0 and (k - counts)%2 == 0:
    print('Yes')
else:
    print('No')

# pythonだとTLE、pypyだとAC
# わざわざ操作しなくても引き算でcountsは求まる。
