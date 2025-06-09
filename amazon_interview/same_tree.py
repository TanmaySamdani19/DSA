def solution(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return solution(p.left, q.left) and solution(p.right, q.right)