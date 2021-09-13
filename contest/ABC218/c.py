n = int(input())
s = list(input().split() for _ in range(n))
t = list(input().split() for _ in range(n))


# 不要な部分は削除
s_new = [[] for _ in range(n)]
t_new = [[] for _ in range(n)]

for i in range(n):
    if s[i] != ['.'*n]:
        for word in s[i][0]:
            s_new[i].append(word)

for i in range(n):
    if t[i] != ['.'*n]:
        for word in t[i][0]:
            t_new[i].append(word)

s_new = [i for i in s_new if i != []]
t_new = [i for i in t_new if i != []]


# sのみ転置して一致するか判定する
super_judge = False
for _ in range(4):
    judge = False

    s_index = [[] for _ in range(n)]
    t_index = [[] for _ in range(n)]

    s_new_t = [list(x) for x in zip(*s_new)]

    for i, word_list in enumerate(s_new_t):
        for j, word in enumerate(word_list):
            if word == '#':
                s_index[i].append(j)

    for i, word_list in enumerate(t_new):
        for j, word in enumerate(word_list):
            if word == '#':
                t_index[i].append(j)

    s_index = [i for i in s_index if i != []]
    t_index = [i for i in t_index if i != []]

    judge = []
    for i, num_list in enumerate(s_index):
        for j in range(n):
            try:
                if t_index[i] == list(map(lambda x: x+j, num_list)):
                    judge.append('True')
                if t_index[i] == list(map(lambda x: x-j, num_list)):
                    judge.append('True')
            except IndexError:
                pass

    if len(judge) == len(s_index):
        super_judge = True
        break

if super_judge == True:
    print('Yes')
else:
    print('No')
