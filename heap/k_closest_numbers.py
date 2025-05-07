import heapq

def k_closest_numbers(arr, target, k):
    if k <= 0 or k > len(arr):
        return []
    
    max_heap = []
    for num in arr:
        diff = abs(num -target)
        heapq.heappush(max_heap, (-diff, -num))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    
    result = []
    while max_heap:
        result.append(-heapq.heappop(max_heap)[1])

    return result[::-1]

arr = [1, 2, 3, 4, 5]
k = 3
target = 3
print(k_closest_numbers(arr, target, k))