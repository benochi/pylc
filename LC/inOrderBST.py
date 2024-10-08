# left, node, right so everything is in order.
# bst traversal = 0(nlogn)
# PREORDER Traversal print root, then print left, then print right.
# For Preorder, print, root.left, root.right, print
# post order, is opposite, root.left, root.right, root
# reverse right, print, left.


def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)
