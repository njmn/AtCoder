#https://atcoder.jp/contests/abs/tasks/abc081_b

input()
input_list=input().split(" ")

def return_even_list(input_list):
    return_list =[]
    for i in input_list:
        if int(i)%2==0:
            return_list.append(int(i)/2)
        else:
            return []
    return return_list

count=0
while True:
    input_list=return_even_list(input_list)
    if not input_list:
        break
    # print(input_list)
    count+=1

print(count)
