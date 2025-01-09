class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class Queue:
  def __init__(self):
    self.head = self.tail = None
    self.length = 0
    
  def enqueue(self,item):
    newNode = Node(item)
    if not self.head:
      self.head = self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode
    self.length += 1

  def deque(self):
    if not self.head:
      return None
    removed = self.head
    self.head = self.head.next
    self.length -= 1
    if not self.head:
      self.tail = None
    return removed.val
  
  def peek(self):
    if not self.head:
      return None
    return self.head.val
  
  def getLength(self):
    return self.length
  
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())        # Output: 1
print(q.deque())       # Output: 1
print(q.getLength())   # Output: 2
print(q.deque())       # Output: 2
print(q.deque())       # Output: 3
print(q.getLength()) 