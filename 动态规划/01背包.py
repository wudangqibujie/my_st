W = 4
wt = [2, 1, 3]
val = [4, 2, 3]


def solution():
    dp = [[0 for _ in range(W + 1)] for _ in range(len(wt) + 1)]

    for i in range(1, len(wt) + 1):
        for j in range(1, W + 1):
            choi1 = dp[i - 1][j]
            choi2 = dp[i - 1][j - wt[i - 1]] + val[i - 1] if j >= wt[i - 1]  else 0
            dp[i][j] = max(choi1, choi2)
    return dp[-1][-1]

print(solution())