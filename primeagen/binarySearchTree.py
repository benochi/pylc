#BST
#left LTE, right RTE sometimes you do L<= root <= right(if you have a bunch of the middle value)
#similar to quickSort. Root would be pivot. 

#balacned tree O(log n)  unbalanced O(n)       Good answer: (log n) - O(N)
from collections import deque

def bstSearch(node, v):
  if not node:
    return False
  
  if node.val == v:
    return node.val
  if node.val < v:
    return bstSearch(node.right, v)
  else:
    return bstSearch(node.left, v)
  
def bstInsert(node, value):
  if not node:
     return TreeNode(value)
  
  if value <= node.val:
    node.left = bstInsert(node.left, value)
  else:
    node.right = bstInsert(node.right, value)

  return node

def bstDelete(node, value):
  return

def printTreeInOrder(node):
  if not node:
    return
  printTreeInOrder(node.left)
  print(node.val, end=" ")
  printTreeInOrder(node.right)

def printTreePreOrder(node):
  if not node:
    return
  print(node.val, end=" ")
  printTreePreOrder(node.left)
  printTreePreOrder(node.right)

def printTreePostOrder(node):
  if not node:
    return
  printTreePostOrder(node.left)
  printTreePostOrder(node.right)
  print(node.val, end=" ")

def printLevelOrder(root):
  if not root: 
    return
  q = deque([root])
  while q:
    level = len(q)
    for i in range(level):
      node = q.popleft()
      print(node.val, end=" ")
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    print()
  




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Build a sample BST
root = TreeNode(10)
root = bstInsert(root, 5)
root = bstInsert(root, 15)
root = bstInsert(root, 3)
root = bstInsert(root, 7)
root = bstInsert(root, 18)
root = bstInsert(root, 12)

# Search
print(bstSearch(root, 7))  # Output: 7
print(bstSearch(root, 9))  # Output: False
print(bstSearch(root, 5))  # Output: 5

printTreeInOrder(root)
print()
printTreePreOrder(root)
print()
printTreePostOrder(root)
printLevelOrder(root)
