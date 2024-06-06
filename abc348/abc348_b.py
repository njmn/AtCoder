n = int(input())

xy_list = []
for i in range(n):
    xy=list(map(int,input().split()))
    xy_list.append(xy)

for i in range(n):
    # indexと座標
    max = [0,0]
    for j in range(n):
        if i == j:
            continue
        x1,y1 = xy_list[i]
        x2,y2 = xy_list[j]
        # ユークリッド距離
        d = ((x1-x2)**2 + (y1-y2)**2)**0.5
        if d > max[1]:
            max = [j,d]
    print(max[0]+1)