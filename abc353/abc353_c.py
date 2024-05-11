n = int(input())
a_list = sorted(list(map(int, input().split())))

a_sum = sum(a_list)
result_b_mod = a_sum * (n - 1)


def count_pairs_exceeding_limit(a_list, limit=10**8):
    count = 0
    n = len(a_list)
    for i in range(n):
        left, right = i + 1, n - 1
        while left <= right:
            mid = (left + right) // 2
            if a_list[i] + a_list[mid] >= limit:
                right = mid - 1
            else:
                left = mid + 1
        count += n - left
    return count


count = count_pairs_exceeding_limit(a_list)
print(result_b_mod - (10**8 * count))
