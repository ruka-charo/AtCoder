n, k = map(int, input().split())


def DeciamlToNine(num):
    "10進数を9進数に変換する"
    nine_number = ""
    while num > 0:
        nine_number += str(num % 9)
        num //= 9
    return int(nine_number[::-1])


for _ in range(k):
    if n == 0:
        break

    m = int(f'{n}', 8) # 10進数表記
    m = str(DeciamlToNine(m)) # 9進数表記
    n = m.replace('8', '5') # 書き換え

print(int(n))
