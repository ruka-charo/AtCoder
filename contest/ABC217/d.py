import bisect

l, q = map(int, input().split())
cx = [map(int, input().split()) for _ in range(q)]
c, x = map(list, zip(*cx))


cut_position = [l]
for i in range(q):
    if c[i] == 1:
        cut_position.append(x[i])
    else:
        cut_position = sorted(cut_position) # ここをどうするか
        index = bisect.bisect_left(cut_position, x[i])
        if index == 0:
            print(cut_position[index])
        else:
            print(cut_position[index] - cut_position[index-1])
