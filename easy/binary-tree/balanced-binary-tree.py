from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            return max(left_height, right_height) + 1

        def is_balanced_helper(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            left_height = height(node.left)
            right_height = height(node.right)
            if abs(left_height - right_height) > 1:
                return False
            return is_balanced_helper(node.left) and is_balanced_helper(node.right)

        return is_balanced_helper(root)


# Runtime 51 ms / Memory 17.50 mb
