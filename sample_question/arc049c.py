# 変数
s = input()


answer = ''
count = 0

while len(answer) < len(s):
    if s[count:count+7] == 'dreamer':
        if s[count+7:count+10] == 'ase':
            answer += 'dream'
            count += 5
        else:
            answer += 'dreamer'
            count += 7

    elif s[count:count+6] == 'eraser':
        answer += 'eraser'
        count += 6

    elif s[count:count+5] == 'erase':
        answer += 'erase'
        count += 5

    elif s[count:count+5] == 'dream':
        answer += 'dream'
        count += 5

    else:
        break


if answer == s:
    print('YES')
else:
    print('NO')
