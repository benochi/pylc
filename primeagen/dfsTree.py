def compareTrees(a, b): #a and b are binary trees we're checking to see if they are the same shape and size
  if a == None and b == None:
    return True
  
  if a == None or b == None:
    return False
  
  if a.value != b.value:
    return False
  
  return compareTrees(a.left, b.left) and compareTrees(a.right, b.right)
  
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Tree 1
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

# Tree 2
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

# Tree 3 (different structure)
tree3 = TreeNode(1)
tree3.left = TreeNode(2)

# Call the function
print(compareTrees(tree1, tree2)) # True (same shape and size)
print(compareTrees(tree1, tree3)) # False