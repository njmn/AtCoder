n, m = map(int, input().split())

# m*mの2次元配列を作成
graph = [[0 for i in range(n)] for j in range(n)]

# グラフに隣接行列を代入
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] += 1
    graph[b-1][a-1] += 1

# 愚直に解いてみる
# 2次元配列の中で、1行ずつ見ていく
count=0

new_graph = graph.copy()
for i,tmp_list in enumerate(graph):
    friend_index_set_1 = set([i for i,x in enumerate(tmp_list) if x == 1])
    for j in range(len(tmp_list)):
        if i == j:
            continue
        if new_graph[i][j] == 0:
            friend_list=new_graph[j]
            friend_index_set = set([i for i, x in enumerate(friend_list) if x == 1])
            if friend_index_set_1 & friend_index_set:
                new_graph[i][j] = 1
                new_graph[j][i] = 1
                count+=1

print(count)
#TLEになる