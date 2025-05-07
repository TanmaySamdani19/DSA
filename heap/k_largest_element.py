import heapq

def k_largest_elements(arr, k):
    if k > len(arr) or k <= 0:
        return []

    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Heap contains the k largest elements (in no particular order)
    return min_heap 
# Test
arr = [7, 10, 4, 3, 20, 15]
k = 3
print("K largest elements:", k_largest_elements(arr, k))  # Output: [20, 15, 10]
