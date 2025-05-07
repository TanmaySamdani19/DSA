import heapq

def frequency_sort(arr):
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    max_heap = []
    for num, freq in frequency.items():
        # Push negative values to simulate a max-heap
        heapq.heappush(max_heap, (-freq, -num))  # If tie in freq, higher num first

    result = []
    while max_heap:
        freq, num = heapq.heappop(max_heap)
        for i in range(-freq):
            result.append(-num)  # Undo the negation

    return result

# Test
arr = [1, 1, 1, 2, 3, 3, 4]
print(frequency_sort(arr))  # Output: [1, 1, 1, 3, 3, 4, 2]
