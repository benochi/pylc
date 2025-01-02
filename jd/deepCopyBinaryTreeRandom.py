# Deep Copy of a Binary Tree with Random Pointers
# Medium

# You are given a binary tree where each node contains the following attributes
# - val: an integer representing the value of the node
# - left: a pointer to the left child
# - right: a pointer to the right child
# - random: a pointer to any node in the tree (or None)

# Construct a deep copy of the binary tree. The deep copy should have exactly the same structure and random pointers as the original tree, but with new nodes.

# Example:

# Input:
# Tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
# random pointers:
# 1.random --> 3
# 2.random --> 6
# 3.random --> None
# 4.random --> 5
# 5.random --> 1
# 6.random --> 4
# 7.random --> 2

# Output:
# A new tree with the same structure and random pointers, but all nodes are new objects

# Constraints:
# 1. The number of nodes in the tree is in the range [0, 1000]
# 2. The random pointer of each node may point to any node in the tree or None


class TreeNode:
  def __init__(self, val=0, left=None, right=None, random=None):
      self.val = val
      self.left = left
      self.right = right
      self.random = random

def makeCopy(self, root):
    if not root:
        return None

    nodeMap = {}

    def dfs(node):
        if not node:
            return None
        
        if node in nodeMap:
            return nodeMap[node]
        
        newNode = TreeNode(node.val)
        nodeMap[node] = newNode

        newNode.left = dfs(node.left)
        newNode.right = dfs(node.right)
        newNode.random = dfs(node.random)
        
    return dfs(root)