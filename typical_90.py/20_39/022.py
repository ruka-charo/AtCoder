import functools
import math

a, b, c = map(int, input().split())


num_list = [a, b, c]
list_gcd = functools.reduce(math.gcd, num_list)


counts = ((a//list_gcd)-1) + ((b//list_gcd)-1) + ((c//list_gcd)-1)
print(counts)
