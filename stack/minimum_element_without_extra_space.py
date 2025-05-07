stack = []
minimum = None

def push(x):
    global minimum
    if not stack:
        stack.append(x)
        minimum = x
    else:
        if x >= minimum:
            stack.append(x)
        else:
            # Encode the new minimum
            stack.append(2 * x - minimum)
            minimum = x

def pop():
    global minimum
    if not stack:
        return -1
    top = stack.pop()
    if top >= minimum:
        return top
    else:
        # Recover the previous minimum
        prev_min = 2 * minimum - top
        popped_value = minimum
        minimum = prev_min
        return popped_value

def get_minimum():
    if not stack:
        return -1
    return minimum

def top():
    if not stack:
        return -1
    if stack[-1] >= minimum:
        return stack[-1]
    else:
        return minimum

# Test
arr = [18, 19, 29, 15, 16]
for i in arr:
    push(i)
print(get_minimum())  # Output: 15
