def solution(p):
    if not p:
        return True
    return isMirror(p.left, p.right)

def isMirror(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return (left.val == right.val and
            isMirror(left.left, right.right) and
            isMirror(left.right, right.left))
