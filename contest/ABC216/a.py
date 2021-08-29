# 10分

a = float(input())
a = int(a*10)
a = str(a)


if 0 <= int(a[-1]) <= 2:
    print(f'{a[:-1]}-')
elif 3 <= int(a[-1]) <= 6:
    print(a[:-1])
elif 7 <= int(a[-1]) <= 9:
    print(f'{a[:-1]}+')
