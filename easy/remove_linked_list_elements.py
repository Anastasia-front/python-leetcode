# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Handle the case where the head is None
        while head is not None and head.val == val:
            head = head.next

        # Iterate through the list to remove nodes with the specified value
        current = head
        while current is not None and current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head


# Runtime 39 ms / Memory 19.32 mb
