# binary tree but sorted.
# all left values must be less than root node all right must be higher
# generally should never contain duplicate values.
# bsts are recursive.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self.insertRecursive(self.root, val)

    def insertRecursive(self, node, val):
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self.insertRecursive(node.left, val)
        elif val > node.val:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self.insertRecursive(node.right, val)
        # don't do anything for matching values to prevent duplicates.

    def search(self, root, target):
        if not root:
            return False

        if target > root.val:
            return self.search(root.right, target)
        elif target < root.val:
            return self.search(root.left, target)
        else:
            return True

    def inOrderTraverse(self):
        result = []
        self.inOrderTraversal(self.root, result)
        return result

    def inOrderTraversal(self, node, result):
        if node:
            self.inOrderTraversal(node.left, result)
            result.append(node.val)
            self.inOrderTraversal(node.right, result)


bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Search for values
print(bst.search(bst.root, 4))  # Output: True
print(bst.search(bst.root, 10))  # Output: False

# Get all values in sorted order
print(bst.inOrderTraverse())
