class Node:
  def __init__(self, val):
    self.val = val
    # if DOUBLY, self.next = next
    self.prev = None

class stack:
  def __init__(self):
    self.head = None
    self.length = 0
  
  def peek(self):
    if self.head:
      return self.head.val
  
  def push(self, val):
    newNode = Node(val)
    if self.head:
      self.head.prev = newNode
    self.head = newNode
    self.length += 1
  
  def pop(self):
    if not self.head:  
        return None
    value = self.head.val
    self.head = self.head.prev
    self.length -= 1
    return value
