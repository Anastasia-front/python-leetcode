from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: If both nodes are None, they are the same
        if not p and not q:
            return True
        # If one of the nodes is None while the other is not, they are different
        elif not p or not q:
            return False
        # If the values are different, the trees are not the same
        elif p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Runtime 30 ms / Memory 16.46 mb
