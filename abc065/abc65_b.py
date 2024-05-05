import sys
sys.setrecursionlimit(1000000)

n = int(input())

a_list = []
for _ in range(n):
    a_list.append(int(input()))

def dfs(n ,count,passed):
    if n == 2:
        return count
    if n in passed:
        return -1
    passed.add(n)
    return dfs(a_list[n-1], count+1, passed)

passed=set()
print(dfs(1,0,passed))