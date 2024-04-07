# https://atcoder.jp/contests/abs/tasks/abc088_b

n = int(input())
a_list = list(map(int, input().split(" ")))
a_list.sort(reverse=True)

# print(a_list)
alice = 0
bob = 0
for i in range(0,n,2):
    alice += a_list[i]
    if n > i+1:
        bob += a_list[i+1]
print(alice - bob)