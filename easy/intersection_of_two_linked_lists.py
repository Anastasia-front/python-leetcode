from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # Helper function to get the length of a linked list
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        # Get the lengths of both linked lists
        length_A = get_length(headA)
        length_B = get_length(headB)

        # Calculate the difference in lengths
        diff = abs(length_A - length_B)

        # Traverse the longer list by the difference
        longer_list = headA if length_A > length_B else headB
        shorter_list = headB if length_A > length_B else headA
        for _ in range(diff):
            longer_list = longer_list.next

        # Traverse both lists simultaneously until intersection is found
        while longer_list and shorter_list:
            if longer_list == shorter_list:
                return longer_list
            longer_list = longer_list.next
            shorter_list = shorter_list.next

        # If no intersection is found, return None
        return None


# Runtime 80 ms / Memory 27.07 mb
