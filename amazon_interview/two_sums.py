# Brute force solution to solve the two sum problem.
def solution(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]       
    return None

# Optimized solution to solve using a hash map time complexity o(n) and space complexity o(n)
def solve(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        # store the index of the current number
        num_map[num] = i
    return None

