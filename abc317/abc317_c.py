n,m=map(int,input().split())
E=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
  a,b,c=map(int,input().split())
  E[a][b]=c
  E[b][a]=c

ans=0
# 街を通ったかどうかのフラグリスト。
used=[False]*(n+1)

# v:現在の頂点 s:現在の距離
def dfs(v,s):
  global ans
  used[v]=True
  if s>ans:
    ans=s
  for i in range(1,n+1):
    if not used[i] and E[v][i]:
      dfs(i,s+E[v][i])
  used[v]=False


for i in range(1,n+1):
  dfs(i,0)

print(ans)