import heapq

def k_frequent_numbers(arr, k):
    if k <= 0 or k > len(arr):
        return []
    
    frequency_map = {}
    for num in arr:
        frequency_map[num] = frequency_map.get(num, 0)+ 1 # here using 0 as default value if key not found

    min_heap = []
    for num, freq in frequency_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap)[1])
    return result[::-1]

arr = [1, 1, 1, 2, 2, 3, 4]
k = 2
print(k_frequent_numbers(arr, k))