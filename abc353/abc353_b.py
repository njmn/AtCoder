n, k = map(int, input().split())
a_list = list(map(int, input().split()))

count = 0

k_original = k

for i in range(n):
    a = a_list[i]
    if a > k:
        k = k_original - a
        count += 1
        # print("count:", count)
        # print(f"kval:{k}")
        continue
    else:
        k -= a
        # print("count:", count)
        # print(f"kval:{k}")


print(count + 1)
