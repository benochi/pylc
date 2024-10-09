# binary tree but sorted.
# all left values must be less than root node all right must be higher
# generally should never contain duplicate values.
# bsts are recursive.
# can be the underlying structure behind sets and maps.
# but can be implemented in other ways

# treemap - from sortedcontainers import SortedDict
# treemap = SortedDict({'c':3, 'a': 1})


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

    def insertRecursive(self, root, val):
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertRecursive(root.right, val)
        elif val < root.val:
            root.left = self.insertRecursive(root.left, val)
        return root
        # don't do anything for matching values to prevent duplicates.

    # can search for val or node
    def minValueNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def maxValueNode(self, root):
        curr = root
        while curr and curr.right:
            curr = curr.right
        return curr

    def remove(self, root, target):
        if not root:
            return None

        if target > root.val:
            root.right = self.remove(root.right, target)
        elif target < root.val:
            root.left = self.remove(root.left, target)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.minValueNode(root.right)
                root.val = minNode.val
                root.right = self.remove(root.right, minNode.val)
        return root

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
