#多重ループを使う場合、indexを作る
h,w = map(int, input().split())

original=[]
row_sums = [0]*h
col_sums = [0]*w

for i in range(h):
    row=list(map(int,input().split()))
    original.append(row)
    row_sums[i] = sum(row)
    for j in range(w):
        col_sums[j]+=row[j]

for i in range(h):
    for j in range(w):
        print(row_sums[i]+col_sums[j]-original[i][j],end=" ")
    print()