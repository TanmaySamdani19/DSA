import heapq

def kth_smallest(arr, k):
    if k > len(arr) or k <= 0:
        return None
    max_heap = []
    
    for i in range(len(arr)):
        heapq.heappush(max_heap, -arr[i])
        if len(max_heap) >k:
            heapq.heappop(max_heap)
        return -max_heap[0]
    
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_smallest(arr,k))