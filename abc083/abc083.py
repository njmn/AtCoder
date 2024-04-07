#https://atcoder.jp/contests/abs/tasks/abc083_b

n,a,b=map(int,input().split(" "))

def jud(n):
    return sum([int(i) for i in str(n)])

answer_list=[]
for i in range(1, n+1):
    num=jud(i)
    if a<=num<=b:
        answer_list.append(i)
print(sum(answer_list))