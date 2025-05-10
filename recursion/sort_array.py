def sort_array(arr):
    if len(arr) == 1:
        return arr
    last = arr.pop()
    sorted_arr = sort_array(arr)
    return insert(sorted_arr, last)

def insert(arr, val):
    if not arr or arr[-1] <= val:
        arr.append(val)
        return arr
    last = arr.pop()
    insert(arr, val)
    arr.append(last)
    return arr

arr = [5, 2, 9, 1, 5, 6]
print(sort_array(arr))
