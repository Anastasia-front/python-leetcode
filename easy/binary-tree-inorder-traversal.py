from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            # Traverse left until no more left nodes
            while current:
                stack.append(current)
                current = current.left

            # Pop from stack and visit the node
            current = stack.pop()
            result.append(current.val)

            # Move to the right subtree
            current = current.right

        return result


# Runtime 29 ms / Memory 16.59 mb

solution = Solution()
nums1 = [1, 0, 2, 3]
print(solution.inorderTraversal(nums1))
