# https://atcoder.jp/contests/abs/tasks/arc065_a
_ = input()
input_list_str=input()
input_list=input_list_str.split()
result=0
for i in input_list:
    result+=int(i)

print(-1*result)
