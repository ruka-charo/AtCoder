n = int(input())
s = list(input().split() for _ in range(n))
t = list(input().split() for _ in range(n))


#%% 文字列を分解する
s_new = [[] for _ in range(n)]
t_new = [[] for _ in range(n)]

for i in range(n):
    for word in s[i][0]:
        s_new[i].append(word)

for i in range(n):
    for word in t[i][0]:
        t_new[i].append(word)

s_new = [i for i in s_new if i != []]
t_new = [i for i in t_new if i != []]


# 座標に置き換える
s_xy = []
t_xy = []

for i in range(n):
    for j in range(n):
        if s_new[i][j] == '#':
            s_xy.append([i+1, j+1])

for i in range(n):
    for j in range(n):
        if t_new[i][j] == '#':
            t_xy.append([i+1, j+1])


# 90°回転の関数
def rotate90(xy_list):
    xy_list_90 = []
    for i in range(len(xy_list)):
        xy_list_90.append([xy_list[i][1], -xy_list[i][0]])

    return xy_list_90

# 平行移動の関数
def slide(xy_list):
    xy_list_slide = []
    x_min = 200
    y_min = 200
    for i in range(len(xy_list)):
        if x_min > xy_list[i][0]:
            x_min = xy_list[i][0]
        if y_min > xy_list[i][1]:
            y_min = xy_list[i][1]

    # 最小座標分だけ平行移動する
    for i in range(len(xy_list)):
        xy_list_slide.append([xy_list[i][0] - x_min, xy_list[i][1] - y_min])

    return xy_list_slide


# 座標の判定
for _ in range(4):
    # 平行移動する
    s_xy, t_xy = slide(s_xy), slide(t_xy)

    if sorted(s_xy) == sorted(t_xy):
        exit(print('Yes'))

    else:
        # 90°回転する
        t_xy = rotate90(t_xy)


print('No')
