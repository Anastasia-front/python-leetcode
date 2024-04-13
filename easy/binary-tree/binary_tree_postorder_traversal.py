from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = []
        visited = set()

        while stack or root:
            # Traverse to the leftmost node
            while root:
                stack.append(root)
                root = root.left

            # Peek at the top node of the stack
            peek_node = stack[-1]

            # If the right child exists and is not visited yet, traverse to it
            if peek_node.right and peek_node.right not in visited:
                root = peek_node.right
            else:
                # If the right child is visited or doesn't exist, process the node
                result.append(peek_node.val)
                visited.add(peek_node)
                stack.pop()

        return result


# Runtime 30 ms / Memory 16.56 mb
