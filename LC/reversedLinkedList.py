class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use two pointers for iterative approach
        prev, curr = None, head

        while curr:
            # Store next into variable
            nxt = curr.next
            # change pointer to prev
            curr.next = prev
            # change prev to current node
            prev = curr
            # change current node to original next node
            curr = nxt

        # return prev this will be the head of the reversed list.
        return prev

    # # RECURSIVE:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # Recursive version
    #     if not head:
    #         return None

    #     newHead = head
    #     if head.next:
    #         newHead = self.reverseList(head.next)
    #         head.next.next = head
    #     head.next = None

    #     return newHead
