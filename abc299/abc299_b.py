import sys


n, t = map(int, input().split())
c_list = list(map(int, input().split()))
r_list = list(map(int, input().split()))

if t in c_list:
    tar_col = t
else:
    tar_col = c_list[0]

ans_list = [r_list[i] for i, x in enumerate(c_list) if x == tar_col]
ans_list.sort()
tar_val = ans_list[-1]

print(r_list.index(tar_val) + 1)
