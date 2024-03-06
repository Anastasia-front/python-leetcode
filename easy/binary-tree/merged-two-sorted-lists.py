from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Placeholder for the merged result
        merged_result = ListNode()
        current = merged_result

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Handle remaining nodes in list1 or list2
        current.next = list1 or list2

        return merged_result.next


# Runtime 32 ms / Memory 16.66 mb
solution = Solution()

print("Solution - Runtime 32 ms / Memory 16.66 mb")
print(solution.mergeTwoLists([1, 2, 3, 4], [2, 3, 4, 5]))


class MySolution:
    def mergeTwoLists(self, list1: list, list2: list) -> list:
        list1.extend(list2)
        list1.sort()
        return list1


# Runtime 36 ms / Memory 16.67 mb
mySolution = MySolution()

print("MySolution - Runtime 36 ms / Memory 16.67 mb")
print(mySolution.mergeTwoLists([1, 2, 4], [1, 3, 4]))
