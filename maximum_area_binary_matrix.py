def maximum_area_binary_matrix(matrix):
    if not matrix or not matrix[0]:
        return 0

    def maximum_area_histogram(heights):
        stack = []
        size = len(heights)
        left = []
        right = []
        width = []
        area = []

        # Nearest Smaller to Left (NSL)
        for i in range(size):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if not stack:
                left.append(-1)
            else:
                left.append(stack[-1][1])
            stack.append((heights[i], i))

        # Clear stack for NSR
        stack = []

        # Nearest Smaller to Right (NSR)
        for i in range(size - 1, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if not stack:
                right.append(size)
            else:
                right.append(stack[-1][1])
            stack.append((heights[i], i))

        right.reverse()  # To match original order

        for i in range(size):
            width.append(right[i] - left[i] - 1)
            area.append(width[i] * heights[i])

        return max(area)

    # First row becomes initial histogram
    vector = matrix[0][:]
    max_area = maximum_area_histogram(vector)

    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                vector[j] = 0
            else:
                vector[j] += 1
        max_area = max(max_area, maximum_area_histogram(vector))

    return max_area

# Example matrix
matrix = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]

print(maximum_area_binary_matrix(matrix))  # Output: 8
