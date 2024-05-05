n=int(input())

dif=-1
a_sum=0
for i in range(n):
    a,b=map(int,input().split())
    a_sum+=a
    new_dif=b-a
    if new_dif>dif:
        dif=new_dif

print(a_sum+dif)