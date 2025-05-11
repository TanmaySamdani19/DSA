def kth_symbol(n, k):
    if n == 1 and k == 1:
        return 0
    length = 2 ** (n - 1)
    mid = length // 2
    if k <= mid:
        return kth_symbol(n - 1, k)
    else:
        return 1 - kth_symbol(n - 1, k - mid)
    
print(kth_symbol(4, 3))