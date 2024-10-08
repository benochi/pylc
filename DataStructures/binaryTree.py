# left child and right child. without children they are Leaf Nodes.
# nodes can also have parent nodes. Binary trees can't have cycles.
# Top node is ROOT node
# Nodes that share a parent are called sibling nodes
# nodes have a HEIGHT property. single node = 1. from node to lowest
# descendant which could be any child or grandchild, etc...
# ancestor refers to parent node chain.

# DEPTH - opposite of height, goes towards root, since everything is
# upside down and illogical


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
