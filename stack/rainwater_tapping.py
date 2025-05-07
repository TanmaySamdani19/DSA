def rainwater_tapping(height):
    n = len(height)
    if n == 0:
        return 0

    # Initialize max_left and max_right with zeros
    max_left = [0] * n
    max_right = [0] * n

    # Fill max_left
    max_left[0] = height[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], height[i])

    # Fill max_right
    max_right[-1] = height[-1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], height[i])

    # Calculate trapped water
    water = 0
    for i in range(n):
        water += min(max_left[i], max_right[i]) - height[i]

    return water

# Example usage
height = [3, 0, 0, 2, 0, 4]
print(rainwater_tapping(height))  # Output: 10
