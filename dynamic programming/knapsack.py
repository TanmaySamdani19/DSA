def solve():
    weight = [1, 2, 3, 4, 5]
    value = [10, 15, 40, 50, 100]
    W = 7
    n = len(weight)
    dp = [[0 for _ in range(W + 1)] for _ in range(n+1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weight[i - 1] <= w:
                dp[i][w] = max(value[i - 1] + dp[i - 1][weight[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

            return dp[n][w]

print(solve())