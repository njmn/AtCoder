from collections import deque

s=deque(input())
t=deque(input())

count=1
while s:
    # print(f"count:{count}")
    s_pop=s.popleft()
    # print("s_pop:{s_pop}".format(s_pop=s_pop))
    while t:
        count+=1
        t_pop=t.popleft()
        # print("t_pop:{t_pop}".format(t_pop=t_pop))
        if s_pop==t_pop:
            print(f"{count-1} ",end="")
            break
        