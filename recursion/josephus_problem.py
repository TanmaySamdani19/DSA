def answer(n,k):
    arr= []
    for i in range(1, n+1):
        arr.append(i)
    index = 0
    ans = []
    solve(arr, k, index, ans)
    return ans[-1]

def solve(arr, k, index, ans):
    if len(arr) == 1:
        ans.append(arr[0])
        return
    index = (index + k -1) % len(arr)
    arr.pop(index)
    solve(arr, k, index, ans)
    return ans

print(answer(40, 7))