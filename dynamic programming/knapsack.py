def solve():
    weight = [1, 2, 3, 4, 5]
    value = [10, 15, 40, 50, 100]
    W = 7
    n = len(weight)
    dp = [[0 for _ in range(W + 1)] for _ in range(n+1)]