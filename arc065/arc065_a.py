# https://atcoder.jp/contests/abs/tasks/arc065_a
s = input()

l1=list("dream")
l2=list("dreamer")
l3=list("erase")
l4=list("eraser")

l1.reverse()
l2.reverse()
l3.reverse()
l4.reverse()

word_list = ["".join(l1),"".join(l2),"".join(l3),"".join(l4)]

s_list=list(s)
s_list.reverse()
s="".join(s_list)

while len(s) > 0:
    flag = False
    for word in word_list:
        if s.startswith(word):
            s = s[len(word):]
            flag = True
            break
    if not flag:
        print("NO")
        exit()
print("YES")