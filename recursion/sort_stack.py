def sort_stack(stack):
    if len(stack) == 1:
        return stack
    last = stack.pop()
    sort_stack(stack)
    insert(stack, last)
    return stack

def insert(stack, val):
    if not stack or stack[-1] >= val:
        stack.append(val)
        return
    last = stack.pop()
    insert(stack, val)
    stack.append(last)

stack = [5, 2, 9, 1, 5, 6]
print(sort_stack(stack))
