def nearest_greater_to_right(arr):
    v = []           # This will store the final result (nearest greater to right)
    s = []           # Stack to keep potential NGR elements
    size = len(arr)

    # We traverse the array from right to left
    for i in range(size - 1, -1, -1):
        # Case 1: If stack is empty, there is no greater element to the right
        if not s:
            v.append(-1)
        
        # Case 2: Top of the stack is greater than current element
        elif s[-1] > arr[i]:
            v.append(s[-1])
        
        # Case 3: Stack has elements, but top is less than or equal to current element
        else:
            # Pop elements from the stack till we find a greater one or it becomes empty
            while s and s[-1] <= arr[i]:
                s.pop()
            
            # If stack becomes empty, no greater element found
            if not s:
                v.append(-1)
            else:
                # Found a greater element on the right
                v.append(s[-1])
        
        # Push the current element onto the stack for future comparisons
        s.append(arr[i])
    
    # Since we were processing from right to left, we reverse the result
    return v[::-1]

arr = [4, 5, 2, 10, 8]
print(nearest_greater_to_right(arr))  # Output: [5, 10, 10, -1, -1]
# Time Complexity : O(n)  - Each element is pushed and popped from the stack at most once.
# Space Complexity : O(n) - Stack can grow up to n elements in the worst case.