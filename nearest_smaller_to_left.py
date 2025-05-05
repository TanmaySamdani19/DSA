def nearest_smaller_to_left(arr):
    v = []
    s = []
    size = len(arr)

    for i in range (size):
        if not s:
            v.append(-1)
        elif s[-1] < arr[i]:
            v.append(s[-1])
        else:
            while s and s[-1] >= arr[i]:
                s.pop()
            if not s:
                v.append(-1)
            else: 
                v.append(s[-1])
        s.append(arr[i])
    return v


arr = [4, 5, 2, 10, 8]
print(nearest_smaller_to_left(arr)) # Output: [-1. 4, -1, 2,2]

