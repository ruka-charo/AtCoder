'''3つ以上の最大公約数'''
import functools
import math

a, b, c = map(int, input().split())


num_list = [a, b, c]
list_gcd = functools.reduce(math.gcd, num_list)
