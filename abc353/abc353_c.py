# 和はlist内の2要素のすべての組み合わせを出せばいい。
# それぞれの要素は、n-1回ずつ出てくるので、全ての和とn-1の積になる。

n = int(input())
a_list = sorted(list(map(int, input().split())))

a_sum = sum(a_list)
sum_all = a_sum * (n - 1)

# ただし、設問は10**8 を超えている場合余りを求めているので、
# 10**8を超える組み合わせの数を求める必要がある。


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

# 10**8を超える回数は、mod 10**8 を行った回数なので、その回数 * 10**8 を引けばいい。
print(sum_all - (10**8 * count))
