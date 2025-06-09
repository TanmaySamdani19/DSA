def solution(p):
    max_diameter = [0]  # use list to allow mutation in nested function

    def depth(node):
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        max_diameter[0] = max(max_diameter[0], left + right)
        return max(left, right) + 1

    depth(p)
    return max_diameter[0]
