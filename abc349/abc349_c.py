s_list = list(input())
t_list = list(input())

last_index = len(s_list) - 1
result_list = [-1]*3

for i, t_val in enumerate(t_list):
    if t_val == "X" and i == 2:
        result_list[i] = last_index
    else:
        t_val = t_val.lower()
        for j, s_val in enumerate(s_list):
            if t_val == s_val and (i == 0 or j > result_list[i-1]):
                result_list[i] = j
                break

if -1 in result_list or sorted(result_list) != result_list:
    print("No")
else:
    print("Yes")