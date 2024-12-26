# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, currentSum):
            if not node:
                return 0
            
            currentSum += node.val
            totalPaths = 1 if currentSum == targetSum else 0
            
            # Continue path with children
            totalPaths += dfs(node.left, currentSum)
            totalPaths += dfs(node.right, currentSum)
            
            return totalPaths
            
        if not root:
            return 0
            
        # Start new path from current node + recursively check all subtrees
        return dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)