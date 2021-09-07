import numpy as np

a, b, c = map(int, input().split())


# 浮動小数点数同士を比較するのは避ける
if a < c**b:
    print('Yes')
else:
    print('No')
