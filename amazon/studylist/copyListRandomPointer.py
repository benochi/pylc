"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return
        
        oldToNew = {}

        current = head

        while current:
            oldToNew[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            copy = oldToNew[current]
            copy.next = oldToNew.get(current.next)
            copy.random = oldToNew.get(current.random)
            current = current.next

        return oldToNew[head]