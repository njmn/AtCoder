import sys
sys.setrecursionlimit(1000000)

import sys

h,w=map(int,input().split())

map_mat = [["#"]*w for _ in range(h)]

for i in range(h):
    input_list = list(input())
    map_mat[i] = input_list
    if "s" in input_list:
        start = [i,input_list.index("s")]

visited_mat = [[False]*w for _ in range(h)]

directions_x = [1,0,-1,0]
directions_y = [0,1,0,-1]

def dfs(vertex):
    '''
    深さ優先探索

    Parameters:
    vertex: 現在の頂点 (x,y)
    sum: 現在の合計値
    result: 結果(gに到達したらTrue)
    '''
    # 到達済みにする
    visited_mat[vertex[0]][vertex[1]] = True
    for direction in range(4):
        # 次の頂点
        next_x = vertex[0]+directions_x[direction]
        next_y = vertex[1]+ directions_y[direction]
        # 範囲外 or 到達済み
        if next_x < 0 or next_x >= h or next_y < 0 or next_y >= w or visited_mat[next_x][next_y]:
            continue
        tar=map_mat[next_x][next_y]
        # 壁
        if tar == "#":
            continue
        # ゴール
        if tar == "g":
            print("Yes")
            sys.exit()
        dfs([next_x,next_y])

dfs(start)

print("No")