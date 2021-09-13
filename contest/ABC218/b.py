p = list(map(int, input().split()))

s = 'abcdefghijklmnopqrstuvwxyz'


word = []
for i in p:
    word.append(s[i-1])

print(''.join(word))
