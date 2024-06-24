grid = []
for _ in range(3):
    grid.append(list(map(int, input().split())))

# 列0と列1の比較
if (
    grid[0][0] - grid[0][1] == grid[1][0] - grid[1][1]
    and grid[0][0] - grid[0][1] == grid[2][0] - grid[2][1]
):
    # 列1と列2の比較
    if (
        grid[0][1] - grid[0][2] == grid[1][1] - grid[1][2]
        and grid[0][1] - grid[0][2] == grid[2][1] - grid[2][2]
    ):
        # 行0と行1の比較
        if (
            grid[0][0] - grid[1][0] == grid[0][1] - grid[1][1]
            and grid[0][0] - grid[1][0] == grid[0][2] - grid[1][2]
        ):
            # 行1と行2の比較
            if (
                grid[1][0] - grid[2][0] == grid[1][1] - grid[2][1]
                and grid[1][0] - grid[2][0] == grid[1][2] - grid[2][2]
            ):
                print("Yes")
                exit()
print("No")
