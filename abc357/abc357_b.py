s = list(input())


# 小文字かどうか判定
def is_lower(s):
    return s.islower()


lower_count = 0
upper_count = 0
for i in s:
    if is_lower(i):
        lower_count += 1
    else:
        upper_count += 1

if lower_count < upper_count:
    # 大文字に変換
    print("".join([i.upper() for i in s]))
else:
    # 小文字に変換
    print("".join([i.lower() for i in s]))
