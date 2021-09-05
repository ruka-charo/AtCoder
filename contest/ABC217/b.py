# 15分

s1 = input()
s2 = input()
s3 = input()
s = [s1, s2, s3]
t = ['ABC', 'ARC', 'AGC', 'AHC']


for i in t:
    if i not in s:
        print(i)
