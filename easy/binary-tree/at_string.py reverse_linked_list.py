from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Approach
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive Approach
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


# Runtime 39 ms / Memory 17.72 mb


# Example usage
# Helper function to create a linked list from a list
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()


# Example 1
head1 = create_linked_list([1, 2, 3, 4, 5])
reversed_head1 = Solution().reverseList(head1)
print_linked_list(reversed_head1)  # Output: 5 4 3 2 1

# Example 2
head2 = create_linked_list([1, 2])
reversed_head2 = Solution().reverseListRecursive(head2)
print_linked_list(reversed_head2)  # Output: 2 1

# Example 3
head3 = create_linked_list([])
reversed_head3 = Solution().reverseList(head3)
print_linked_list(reversed_head3)  # Output: None (empty list)
