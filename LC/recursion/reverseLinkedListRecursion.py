class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = reverseList(head.next)
        # node1.node2.node2next = node1
        head.next.next = head
    # if no head.next set to null for NEW head
    head.next = None
    return newHead


# Helper function to print the linked list
def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next


# Test cases
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head2 = ListNode(0, ListNode(17))

print("Original List 1:")
print_list(head)

reversed_head = reverseList(head)
print("Reversed List 1:")
print_list(reversed_head)

print("Original List 2:")
print_list(head2)

reversed_head2 = reverseList(head2)
print("Reversed List 2:")
print_list(reversed_head2)
