import sys
sys.setrecursionlimit(10000)

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if visited[x][y]:
        return freedom[x][y]
    visited[x][y] = True
    freedom[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or H <= nx or ny < 0 or W <= ny or S[nx][ny] == '#':
            continue
        freedom[x][y] += dfs(nx, ny)
    return freedom[x][y]

freedom = [[0]*W for _ in range(H)]
visited = [[False]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            dfs(i, j)

print(max(max(row) for row in freedom))