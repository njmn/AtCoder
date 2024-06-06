a, b = input().split()

candidate = set([1, 2, 3])

if a != b:
    ans = candidate - set([int(a), int(b)])
    print(ans.pop())
else:
    print(-1)
