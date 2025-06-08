def solution(ratings):
    if not ratings:
        return 0
    
    n = len(ratings)
    candies = [1] * n # start with 1 candy for each child

    # First pass : left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # second pass : right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i +1]:
            candies[i] = max(candies[i], candies[i + 1] + 1) # ensure we keep the max candies

    return sum(candies)