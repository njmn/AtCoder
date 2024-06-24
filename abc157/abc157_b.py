# 3*3 だから愚直にビンゴ判定でOK

card = [list(map(int, input().split())) for _ in range(3)]
n = int(input())

for i in range(n):
    b = int(input())
    for j, line in enumerate(card):
        for k, num in enumerate(line):
            if num == b:
                line[k] = 0

for line in card:
    if not any(line):
        print('Yes')
        exit()

for i in range(3):
    if card[0][i] == 0 and card[1][i] == 0 and card[2][i] == 0:
        print('Yes')
        exit()

if card[0][0] == 0 and card[1][1] == 0 and card[2][2] == 0:
    print('Yes')
    exit()

if card[0][2] == 0 and card[1][1] == 0 and card[2][0] == 0:
    print('Yes')
    exit()

print('No')
