class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

newNode = TreeNode(1)
adjList = {}
adjList[newNode] = "Hello"

print(adjList)