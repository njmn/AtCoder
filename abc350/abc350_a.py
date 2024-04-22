# https://atcoder.jp/contests/abs/tasks/arc065_a
inputstr = input()

num=inputstr[3:]

intnum=int(num)

if 350<=intnum:
    print("No")
elif intnum == 316 or intnum == 0:
    print("No")
else:
    print("Yes")