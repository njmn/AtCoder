import math
import sys
sys.setrecursionlimit(10000)


def update_list(new_list):
    last=new_list[-1]
    new_list[-2:] = [last+1]

n=int(input())
a_list = list(map(int,input().split()))
new_list = []

for i in range(n):
    new_list.append(a_list[i])
    if i == 0:
        continue
    else:
        while new_list[-1] == new_list[-2]:
            update_list(new_list)
            if len(new_list) <=1:
                break
print(len(new_list))