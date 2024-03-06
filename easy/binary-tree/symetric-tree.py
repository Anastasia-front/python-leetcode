from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # Base case: If both nodes are None, they are symmetric
            if not left and not right:
                return True
            # If one of the nodes is None while the other is not, they are not symmetric
            elif not left or not right:
                return False
            # If the values are different, the trees are not symmetric
            elif left.val != right.val:
                return False
            # Recursively check the symmetry of the subtrees
            else:
                return isMirror(left.left, right.right) and isMirror(
                    left.right, right.left
                )

        # Handle the case where the root is None
        if not root:
            return True

        # Check the symmetry starting from the root's left and right subtrees
        return isMirror(root.left, root.right)


# Runtime 36 ms / Memory 16.57 mb
