# https://atcoder.jp/contests/abs/tasks/arc065_a
n,q = input().split()
t_list = list(map(int, input().split()))
t_set = set(t_list)

minus_count = 0
for t in t_set:
    count=t_list.count(t)
    if count%2==1:
        minus_count+=1

# print(minus_count)
print(int(n)-minus_count)