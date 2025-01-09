def compareTrees(a, b): #a and b are binary trees we're checking to see if they are the same shape and size
  if a == None and b == None:
    return True
  
  if a == None or b == None:
    return False
  
  if a.value != b.value:
    return False
  
  return compareTrees(a.left, b.left) and compareTrees(a.right, b.right)
  