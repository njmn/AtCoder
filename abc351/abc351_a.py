import sys
sys.setrecursionlimit(10000)

input_a = map(int,input().split())
input_b = map(int,input().split())

sum_a = sum(input_a)
sum_b = sum(input_b)

print(sum_a-sum_b+1)