import heapq

def k_sorted_array(arr, k):
    if k <= 0 or k >len(arr):
        return arr
    min_heap = []
    result = []
    for i in range(len(arr)):
        heapq.heappush(min_heap, arr[i])
        if len(min_heap) > k:
            result.append(heapq.heappop(min_heap))
    return result + min_heap

arr = [1, 4, 7, 2, 5, 3, 6]
k = 3
print(k_sorted_array(arr, k))