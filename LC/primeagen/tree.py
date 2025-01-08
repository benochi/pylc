# PreOrder  Root left right
# inOrder left root right
# Postorder right left root 

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# In-Order Traversal (Left, Root, Right)
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.value, end=" ")

# Pre-Order Traversal (Root, Left, Right)
def preOrder(root):
    if root:
        print(root.value, end=" ")
        preOrder(root.left)
        preOrder(root.right)

# Post-Order Traversal (Left, Right, Root)
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.value, end=" ")

# Level-Order Traversal (BFS)
from collections import deque

def levelOrder(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.value, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

# Example Tree
#      1
#     / \
#    2   3
#   / \
#  4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform Traversals
print("In-Order: ", end="")
inOrder(root)  # Output: 4 2 5 1 3
print("\nPre-Order: ", end="")
preOrder(root)  # Output: 1 2 4 5 3
print("\nPost-Order: ", end="")
postOrder(root)  # Output: 4 5 2 3 1
print("\nLevel-Order: ", end="")
levelOrder(root)  # Output: 1 2 3 4 5