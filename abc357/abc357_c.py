n = int(input())


def fractal(level):
    if level == 0:
        return [['#']]
    else:
        smaller = fractal(level - 1)
        new_size = len(smaller) * 3
        grid = [['.' for _ in range(new_size)] for _ in range(new_size)]
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                for x in range(len(smaller)):
                    for y in range(len(smaller)):
                        grid[i * len(smaller) + x][j * len(smaller) + y] = smaller[x][y]
        return grid


result = fractal(n)
print(result)
for row in result:
    print(''.join(row))
