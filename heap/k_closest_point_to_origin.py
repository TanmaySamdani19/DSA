import heapq

def k_closest_points(points, k):
    if k <= 0 or k > len(points):
        return []

    max_heap = []
    for point in points:
        distance = point[0]**2 + point[1]**2
        # Use negative distance to simulate a max-heap
        heapq.heappush(max_heap, (-distance, point))
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    # Extract points from the heap
    result = [point for (i, point) in max_heap]
    return result[::-1]

# Example usage
arr = [[1, 2], [3, 4], [5, 6], [7, 8]]
k = 2
print(k_closest_points(arr, k))
