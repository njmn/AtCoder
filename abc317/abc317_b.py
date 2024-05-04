n=int(input())
a_set = set(map(int, input().split()))
minimum = min(a_set)

perfect_a_set=set(range(minimum, minimum+n+1))

result=perfect_a_set-a_set

for i in result:
    print(i)