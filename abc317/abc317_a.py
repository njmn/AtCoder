n,h,x=map(int,input().split())
p_list = list(map(int, input().split()))

tar=x-h

for i,p in enumerate(p_list):
    if p>=tar:
        print(i+1)
        break