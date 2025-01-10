class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Start with height = 1 for new nodes

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, node, value):
        # Standard BST insertion
        if not node:
            return AVLNode(value)
        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        # Update height of the current node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Check balance factor
        balance = self.get_balance(node)

        # Perform rotations to balance the tree
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)  # Left-Left case
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)  # Right-Right case
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)  # Left-Right case
            return self.rotate_right(node)
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)  # Right-Left case
            return self.rotate_left(node)

        return node

    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)

# Example usage:
avl = AVLTree()
root = None
values = [10, 20, 30, 40, 50, 25]

for v in values:
    root = avl.insert(root, v)

print("Inorder Traversal of AVL Tree:", avl.inorder(root))