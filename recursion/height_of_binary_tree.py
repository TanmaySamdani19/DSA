def height_of_binary_tree(root):
    if root is None:
        return 0
    left_height = height_of_binary_tree(root.left)
    right_height = height_of_binary_tree(root.right)
    return max(left_height, right_height) + 1


# Example
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# creating a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)

print(height_of_binary_tree(root))