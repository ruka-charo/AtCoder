import numpy as np

T = int(input())
l, x, y = map(int, input().split())
q = int(input())
e = [int(input()) for _ in range(q)]


# 時刻tの時の観覧車の座標
def yz(t):
    x = 0
    y = -(l/2)*np.sin(t*(2*np.pi)/T)
    z = (l/2)*(1 - np.cos(t*(2*np.pi)/T))

    return x, y, z


for i in range(q):
    # 像の位置座標
    ax, ay, az = x, y, 0
    # 内積から角度を算出する
    bx, by, bz = yz(e[i])

    L = np.sqrt(ax**2 + (by - ay)**2)
    theta = np.degrees(np.arctan(bz/L))

    print(theta)
