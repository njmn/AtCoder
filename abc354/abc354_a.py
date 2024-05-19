n=int(input())

height_list=[1]

count=1
while True:
    if height_list[-1] > n:
        print(count)
        break
    height = height_list[-1] + 2 ** count
    height_list.append(height)
    count += 1

