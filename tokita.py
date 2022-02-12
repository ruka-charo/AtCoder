a = [True,True,False,True,False,False,False,True,True,True]

# リストを文字列に変換(後の処理のため先頭にカンマをつける)
b = ','.join(map(str, a))
b = ',' + b

# 文字列から数えやすいようにリストに分割
c = b.split(',False')

# Falseで区切った配列内の文字列の数をカウント
# ,True → の5文字で1カウントとするので文字数を5で割る
d = list(map(len, c))
e = list(map(lambda x: int(x / 5), d)) #答え
