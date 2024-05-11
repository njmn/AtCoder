import sys


n = input()
h_list = list(map(int, input().split()))

fst = h_list[0]
for i, h in enumerate(h_list):
    if i == 0:
        continue
    if h > fst:
        print(i + 1)
        sys.exit()
print(-1)
