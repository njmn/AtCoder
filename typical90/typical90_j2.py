# https://atcoder.jp/contests/typical90/tasks/typical90_j
# 累積和
n = int(input())
point_list = [[0, 0]]
for i in range(n):
    c, p = map(int, input().split())
    last_point = point_list[-1]
    
    if c == 1:
        new_point = [last_point[0] + p, last_point[1]]
    else:
        new_point = [last_point[0], last_point[1] + p]

    point_list.append(new_point)

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    point_1 = point_list[r][0] - point_list[l-1][0]
    point_2 = point_list[r][1] - point_list[l-1][1]
    print(point_1, point_2)