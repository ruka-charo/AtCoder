import math
a, b = map(int, input().split())


g = math.gcd(a, b) # 最大公約数
# a*b = 最小公倍数 * 最大公約数
l = (a*b) // g


if l > 1e18:
    print('Large')
else:
    print(l)
    
