n = int(input())

dic = {}
sum_val = 0

for i in range(n):
    a, b = input().split()
    b = int(b)
    dic[a] = b
    sum_val += b

key_list = [key for key in dic.keys()]
key_list.sort()

mod_val = sum_val % n

count = 0
for key in key_list:
    if count != mod_val:
        count += 1
        continue
    print(key)
    count += 1
