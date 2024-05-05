n=int(input())
x_list = list(map(int, input().split()))

ave=round(sum(x_list)/n)

print(sum([abs(x-ave)**2 for x in x_list]))