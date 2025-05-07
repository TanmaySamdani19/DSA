import heapq

def connected_ropes(ropes):
    if len(ropes) < 2:
        return 0

    heapq.heapify(ropes)
    total_cost = 0

    while len(ropes) > 1:
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        cost = first + second
        total_cost += cost
        heapq.heappush(ropes, cost)

    return total_cost

# Example usage
arr = [1, 2, 3, 4, 5]
print(connected_ropes(arr))  # Output: 33
