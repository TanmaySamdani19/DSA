def maximum_area_histogram(heights):
    stack = []
    left = []
    right = []
    width = []
    area = []
    size = len(heights)

    # Calculate nearest smaller to left
    for i in range(size):
        while stack and stack[-1][0] >= heights[i]:
            stack.pop()
        if not stack:
            left.append(-1)
        else:
            left.append(stack[-1][1])
        stack.append((heights[i], i))

    stack = []

    # Calculate nearest smaller to right
    for i in range(size - 1, -1, -1):
        while stack and stack[-1][0] >= heights[i]:
            stack.pop()
        if not stack:
            right.append(size)
        else:
            right.append(stack[-1][1])
        stack.append((heights[i], i))

    right.reverse()  # Fix the order of right list

    for i in range(size):
        width.append(right[i] - left[i] - 1)
        area.append(width[i] * heights[i])

    return max(area)

# Test
heights = [6, 2, 5, 4, 5, 1, 6]
print(maximum_area_histogram(heights))  # Output should be 12
