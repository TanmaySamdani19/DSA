def solution(nums1, nums2):
    merged = sorted(num1 + nums2)
    n = len(merged)
    if n % 2 == 0:
        mid1 = n // 2 -1
        mid2 = n // 2
        return (merged[mid1] +merged[mid2]) /2
    else:
        mid = n // 2
        return merged[mid]