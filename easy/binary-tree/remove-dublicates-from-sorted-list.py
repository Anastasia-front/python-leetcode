from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


# Runtime 34 ms / Memory 16.71 mb

# solution = Solution()
# nums1 = [1, 1, 2]
# k1 = solution.deleteDuplicates(nums1)
# print(k1)

# nums2 = [1, 1, 2, 3, 3]
# k2 = solution.deleteDuplicates(nums2)
# print(k2)
