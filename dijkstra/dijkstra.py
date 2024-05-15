# 問題を探して正しいかどうか検証する。あとで。

import heapq


def dijkstra(graph, start, goal):
    n = len(graph)
    # 距離の最短値を格納するリスト
    dist = [float('inf')] * n
    # スタート地点からスタート地点への距離は0
    dist[start] = 0
    # プライオリティキュー (距離, 頂点) の形式で格納する
    q = [(0, start)]
    while q:
        # 距離と現在の頂点。グラフ理論では、現在の頂点をu、次の頂点をvと表すことが多い。
        distance, u = heapq.heappop(q)
        # queueから取り出した頂点がゴールなら、それは確定されている距離のためそのまま返す。
        if u == goal:
            return distance
        # すでに確定している距離よりも大きい距離であれば、更新する必要はない。
        if distance > dist[u]:
            continue
        # 隣接する頂点を探索する
        for v, w in graph[u]:
            # 隣接する頂点への距離が現在の距離よりも小さければ、更新する。
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                # プライオリティキューに追加する
                heapq.heappush(q, (dist[v], v))
    return dist[goal]


# test
graph = [[(1, 1), (2, 4)], [(2, 2)], [(3, 1)], []]
print(dijkstra(graph, 0, 3))
