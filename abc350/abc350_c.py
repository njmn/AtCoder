n = int(input())
raw=list(input().split())
a_list = list(map(int, raw))

index_list = [0] * n
for i in range(n):
    index_list[a_list[i]-1] = i

count = 0
result_list = []
# ソートアルゴリズム
for i in range(1,n+1):
    index = index_list[i-1]
    if index == i-1:
        pass
    else:
        original_num = a_list[i-1]
        a_list[i-1] = i
        a_list[index] = original_num
        index_list[original_num-1] = index
        count+=1
        result_list.append((i,index+1))

#　ソートの回数を出力
print(count)
for i in result_list:
    #ソートの過程を出力
    print(i[0],i[1])