class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result

# Helper function to create a binary tree from a list
def create_binary_tree(nodes, index=0):
    if index < len(nodes) and nodes[index] is not None:
        node = TreeNode(nodes[index])
        node.left = create_binary_tree(nodes, 2 * index + 1)
        node.right = create_binary_tree(nodes, 2 * index + 2)
        return node
    return None

# Create binary tree
root = create_binary_tree([3, 9, 20, None, None, 15, 7])

# Call the levelOrder function
result = levelOrder(root)

# Print the result
print("Level Order Traversal:", result)
