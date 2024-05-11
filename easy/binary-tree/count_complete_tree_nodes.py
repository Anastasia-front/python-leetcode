from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Calculate the depth of the left and right subtrees
        left_depth = self.calculate_depth(root.left)
        right_depth = self.calculate_depth(root.right)

        # If the depth of the left subtree is equal to the depth of the right subtree,
        # it means the left subtree is a full binary tree, and the right subtree is a complete binary tree
        if left_depth == right_depth:
            # Count the nodes in the left subtree (a full binary tree) using the formula 2^depth - 1
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # If the depths are different, the right subtree is a full binary tree, and the left subtree is a complete binary tree
            # Count the nodes in the right subtree (a full binary tree) using the formula 2^depth - 1
            return (1 << right_depth) + self.countNodes(root.left)

    def calculate_depth(self, node: TreeNode) -> int:
        # Helper function to calculate the depth of the subtree
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth


# Runtime 53 ms / Memory 21.91 mb


# Example 1
# Input: root = [1, 2, 3, 4, 5, 6]
# Output: 6
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
print(Solution().countNodes(root1))  # Output: 6

# Example 2
# Input: root = []
# Output: 0
root2 = None
print(Solution().countNodes(root2))  # Output: 0

# Example 3
# Input: root = [1]
# Output: 1
root3 = TreeNode(1)
print(Solution().countNodes(root3))  # Output: 1
