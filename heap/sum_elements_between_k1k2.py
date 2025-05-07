import heapq

def sum_elements_between_k1k2(arr,k1, k2):
    def kth_smallest(arr, k):
        if k > len(arr) or k <= 0:
            return None
        max_heap = []

        for i in range(len(arr)):
            heapq.heappush(max_heap, -arr[i])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return -max_heap[0]
    
    first = kth_smallest(arr, k1)
    second = kth_smallest(arr, k2)
    sum = 0
    for i in arr:
        if i > first and i < second:
            sum += i
    return sum

arr = [1 ,3,12,5,15,11]
k1 = 3
k2 = 6
print(sum_elements_between_k1k2(arr, k1, k2))