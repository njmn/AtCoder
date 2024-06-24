import sys

n, m = map(int, input().split())
h_list = list(map(int, input().split()))

for i, h in enumerate(h_list):
    m -= h
    if m == 0:
        print(i + 1)
        sys.exit()
    elif m < 0:
        print(i)
        sys.exit()

print(len(h_list))
