S = input()

tar = "chokudai"

mod = 10**9 + 7

dp = [[0 for _ in range(len(tar) + 1)] for _ in range(len(S) + 1)]

for i in range(len(S) + 1):
    dp[i][0] = 1

for i in range(len(S)):
    for j in range(len(tar)):
        print(f"update {i+1=},{j+1=},{dp[i+1][j+1]=}")
        if S[i] != tar[j]:
            dp[i + 1][j + 1] = dp[i][j + 1]
            print(f"{dp[i+1][j+1]=}")
        if S[i] == tar[j]:
            dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i][j]) % mod
            print(f"{dp[i][j+1]=},{dp[i][j]=}")

print(f"{dp=}")

print("answer:", dp[len(S)][8])
