def delete_middle(stack, n):
    if n == 0:
        return stack
    k = n // 2 + 1  # 1-based index for middle (for odd lengths)
    solve(stack, k)
    return stack

def solve(stack, k):
    if k == 1:
        stack.pop()
        return
    top = stack.pop()
    solve(stack, k - 1)
    stack.append(top)

stack = [1, 2, 3, 4, 5]
n = len(stack)
print("Stack after deleting middle element:", delete_middle(stack, n))
