from collections import deque
import sys
sys.setrecursionlimit(10000)

h,w=map(int,input().split())

maze=[]

for i in range(h):
    input_list = list(input())
    maze.append(input_list)

directions_x = [1,0,-1,0]
directions_y = [0,1,0,-1]
maximum = 0

maximum = 0

def bfs(start):
    global maximum
    visited_mat = [[False]*w for _ in range(h)]
    distance_mat = [[0]*w for _ in range(h)]
    que = deque([start])
    visited_mat[start[0]][start[1]] = True
    while que:
        vertex = que.popleft()
        for i in range(4):
            next_x = vertex[0] + directions_x[i]
            next_y = vertex[1] + directions_y[i]
            if not (0 <= next_x < h and 0 <= next_y < w) or maze[next_x][next_y] == "#" or visited_mat[next_x][next_y]:
                continue
            visited_mat[next_x][next_y] = True
            distance_mat[next_x][next_y] = distance_mat[vertex[0]][vertex[1]] + 1
            que.append([next_x,next_y])
            maximum = max(maximum, distance_mat[next_x][next_y])

for si in range(h):
    for sw in range(w):
        if maze[si][sw] == "#":
            continue
        bfs([si,sw])

print(maximum)