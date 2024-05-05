div=10**9+7

n,k =map(int,input().split())
a = list(map(int,input().split()))

# BITツリーを使うと早いらしい
# https://www.youtube.com/watch?v=1U6pl4VJ50U
# https://output-zakki.com/inversion_number/
# https://output-zakki.com/binary_indexed_tree/
count = 0
for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            count += 1

# なぜか通らない
print((count+k*count)*k//2)