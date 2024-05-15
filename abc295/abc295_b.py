import copy


r, c = map(int, input().split())

b_list = [["."] * c for _ in range(r)]

for i in range(r):
    b_list[i] = list(input())

copied_b_list = copy.deepcopy(b_list)
for i in range(r):
    for j in range(c):
        bomb = b_list[i][j]
        if bomb.isdigit():
            power = int(bomb)
            for k in range(power + 1):
                # kは爆発の威力（x+y） 0 ~ power まで。
                for l in range(k + 1):
                    # lはxの増加量 0 ~ k まで
                    increment_x = l
                    increment_y = k - l
                    # print(f"{increment_x=}, {increment_y=}")
                    # xが増える、yが増える
                    # print(f"pattern1:{i + increment_x}, {j + increment_y}")
                    if i + increment_x < r and j + increment_y < c:
                        copied_b_list[i + increment_x][j + increment_y] = "."
                    # xが増える、yが減る
                    # print(f"pattern2:{i + increment_x}, {j - increment_y}")
                    if i + increment_x < r and j - increment_y >= 0:
                        copied_b_list[i + increment_x][j - increment_y] = "."
                    # xが減る、yが増える
                    # print(f"pattern3:{i - increment_x}, {j + increment_y}")
                    if i - increment_x >= 0 and j + increment_y < c:
                        copied_b_list[i - increment_x][j + increment_y] = "."
                    # xが減る、yが減る
                    # print(f"pattern4:{i - increment_x}, {j - increment_y}")
                    if i - increment_x >= 0 and j - increment_y >= 0:
                        copied_b_list[i - increment_x][j - increment_y] = "."

for i in copied_b_list:
    print("".join(i))
