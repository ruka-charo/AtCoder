q = int(input())
tx = [map(int, input().split()) for _ in range(q)]
t, x = map(list, zip(*tx))


a = []
b = []
for i in range(q):
    if t[i] == 1:
        b.append(x[i])

    elif t[i] == 2:
        a.append(x[i])

    else:
        if x[i] > len(b):
            print(a[x[i]-len(b)-1])
        else:
            print(b[len(b)-x[i]])


#%% (別解)dequeを用いる
from collections import deque
q = int(input())
tx = [map(int, input().split()) for _ in range(q)]
t, x = map(list, zip(*tx))

a = deque()
for i in range(q):
    if t[i] == 1:
        a.appendleft(x[i])

    elif t[i] == 2:
        a.append(x[i])

    else:
        print(a[x[i]-1])
