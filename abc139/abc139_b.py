a, b = map(int, input().split())

'''
プラグaで増えるコンセントの数は、a-1個(プラグがコンセントを1個つかうため)
目標のコンセント数はb個、増やしたいコンセント数はb-1個（もともと1個のコンセントがあるため、1個減らす）
増やしたいコンセント数/増えるコンセント数を計算することで、必要なプラグの数を求めることができる。
ただし余りがでる場合、プラグが足りていないので、プラグを1個追加する必要がある。
'''

result = (b - 1) // (a - 1)
is_remain = bool((b - 1) % (a - 1))

if is_remain:
    result += 1

print(result)