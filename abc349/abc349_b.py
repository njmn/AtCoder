# https://atcoder.jp/contests/abs/tasks/arc065_a
s = input()

list_s=list(s)

# list_sの要素の数の出現回数をカウント
set_s=set(list_s)

result_dic ={}

for i in set_s:
    # iがlist_sに何回出現するか
    count = list_s.count(i)
    value= result_dic.get(count,0)
    result_dic[count] = value+1


result = True
for i in result_dic.values():
    if i == 2 or i == 0:
        pass
    else:
        result = False
        break

if result:
    print('Yes')
else:
    print('No')
