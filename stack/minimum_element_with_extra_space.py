stack = []
support = []

def push(x):
    stack.append(x)
    if not support or x < support[-1]:
        support.append(x)
    else:
        support.append(support[-1])
    return
    
def pop():
    if not stack:
        return -1
    ans = stack.top()
    stack.pop()
    if support.top() == ans:
        support.pop()
    return ans

def get_minimum():
    if not support:
        return -1
    return support[-1]

arr = [18, 19, 29, 15,16]
for i in arr:
    push(i)
print(get_minimum())