#import sys
#input = sys.stdin.readline

h, w = map(int, input().split())


# 1個飛ばしで点灯していることが最大値の条件
if h == 1 or w == 1:
    print(w * h)

else:
    if w % 2 == 0:
        w_light = w // 2
    else:
        w_light = (w // 2) + 1


    if h % 2 == 0:
        h_light = h // 2
    else:
        h_light = (h // 2) + 1

    # wの並びがh方向に同じように存在する
    print(w_light * h_light)
