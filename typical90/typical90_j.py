n=int(input())

point_list=[]

for i in range(n):
    c,p=map(int,input().split())
    point_list.append([c,p])

q=int(input())

output_list=[]
for i in range(q):
    l,r = map(int,input().split())
    point_1=0
    point_2=0
    for j in range(l-1,r):
        tar_class=point_list[j][0]
        if tar_class==1:
            point_1+=point_list[j][1]
        else:
            point_2+=point_list[j][1]

    output_list.append([point_1,point_2])

for i in output_list:
    print(i[0],i[1])