import numpy as np
n = int(input())


# 素数カウント
def prime_counts(n):
    counts = 0
    root_n = int(np.sqrt(n).round())
    prime = True
    for i in range(2, root_n+1):
        if (n % i == 0):
            prime = False
            while n % i == 0:
                counts += 1
                n //= i

    if n > root_n:
        counts += 1

    if (prime == True) or (n == 2):
        counts = 1

    return counts


# 素因数分解後の素数の数が分かればもとまる
counts = prime_counts(n)

# 2**40 > 1e12
if counts == 1:
    print(0)

for i in range(1, 41):
    if 2**(i-1) < counts <= 2**i:
        print(i)
