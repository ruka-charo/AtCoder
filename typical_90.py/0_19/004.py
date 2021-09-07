x = list(map(int,input().split()))
h, w = x[0], x[1]
a = [list(map(int, input().split())) for l in range(h)]


index_sum = list(map(sum, a))
column_sum = list(map(sum, zip(*a)))


# それぞれの列の合計を求める
for i in range(h):
    ans = map(lambda j: str(index_sum[i] + column_sum[j] - a[i][j]), range(w))
    print(' '.join(ans))
    
