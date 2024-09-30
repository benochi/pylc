class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):

    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next


# Helper function to print the linked list
def print_list(node: ListNode):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next


# Test Case 1: Both lists are empty
list1 = None
list2 = None
print("Test Case 1: Both lists empty")
print_list(mergeTwoLists(list1, list2))  # Output: nothing (empty list)

# Test Case 2: One list is empty
list1 = ListNode(1)
list2 = None
print("Test Case 2: One list empty")
print_list(mergeTwoLists(list1, list2))  # Output: 1

# Test Case 3: Both lists have elements, no overlap
list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))
print("Test Case 3: Both lists have elements, no overlap")
print_list(mergeTwoLists(list1, list2))  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6

# Test Case 4: Lists with some overlapping values
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
print("Test Case 4: Lists with overlapping values")
print_list(mergeTwoLists(list1, list2))  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

# Test Case 5: One list is fully smaller than the other
list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(4, ListNode(5, ListNode(6)))
print("Test Case 5: One list smaller than the other")
print_list(mergeTwoLists(list1, list2))  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
