# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.findMinNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)

        return root

    def findMinNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
