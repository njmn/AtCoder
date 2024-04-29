import sys
sys.setrecursionlimit(10000)

n=int(input())

original_list = []

for i in range(n):
    original_list.append(list(input().split()))


for i in range(n):
    first_input=original_list[i]
    later_input=list(input().split())
    if first_input ==later_input:
        continue
    else:
        for k,j in enumerate(first_input[0]):
            if j != later_input[0][k]:
                print(i+1,k+1)
