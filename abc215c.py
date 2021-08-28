import itertools

# 変数
x = []
a, b=input().split()
x.append([a, int(b)])

s = x[0][0] # 文字列
words = list(s)
k = x[0][1] # 何番目か


# 順列
sentences = [''.join(word) for word in list(set(itertools.permutations(words)))]
# 辞書順にソート
sentences_sort = sorted(sentences)

# 求める答え
print(sentences_sort[k-1])
