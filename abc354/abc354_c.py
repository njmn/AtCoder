from sortedcontainers import SortedList


def filter_cards(cards):
    cards.sort(key=lambda x: (-x[0], x[1]))

    valid_cards = []
    cost_list = SortedList()

    for strength, cost, index in cards:
        if len(cost_list) == 0 or cost < cost_list[0]:
            valid_cards.append((strength, cost, index))
            cost_list.add(cost)

    return valid_cards


n = int(input())
cards = []
for i in range(n):
    a, c = map(int, input().split())
    cards.append((a, c, i + 1))

result = filter_cards(cards)

ans = sorted([index for _, _, index in result])
print(len(ans))
for i in ans:
    print(i, end=" ")
