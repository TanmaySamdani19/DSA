def insert(stack, val):
    if not stack:
        stack.append(val)
        return
    ele = stack.pop()
    insert(stack, val)
    stack.append(ele)
    return stack

def reverse_stack(stack):
    if not stack:
        return stack
    ele = stack.pop()
    reverse_stack(stack)
    insert(stack, ele)
    return stack


stack = [1, 2, 3, 4, 5]
print(reverse_stack(stack))