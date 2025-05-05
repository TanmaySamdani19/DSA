def nearest_smaller_to_right(arr):
    v= []
    s= []
    size = len(arr)

    for i in range(size-1, -1, -1):
        if not s:
            v.append(-1)

        elif s[-1] < arr[i]:
            print(s[0])
            print(s[-1])
            v.append(s[-1])
        else:
            while s and s[-1] >= arr[i]:
                s.pop()
            if not s:
                v.append(-1)
            else:
                v.append(s[-1])
        s.append(arr[i])
    return v[::-1]


arr = [4,5,2,10,8]
print(nearest_smaller_to_right(arr)) # Output: [2,,2, -1, 8, -1]