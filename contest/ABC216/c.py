# 75分

n = int(input())


count = []

for i in range(121): # 120回で終わった時の出力用に+1
    if n == 0 or i == 120:
        print(''.join(count[::-1]))
        break
    elif n % 2 == 0:
        n = int(n / 2)
        count.append('B')
    elif n % 2 == 1:
        n -= 1
        count.append('A')
