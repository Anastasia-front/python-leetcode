from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap the left and right subtrees
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# Runtime 48 ms / Memory 16.70 mb


# Example 1
# Input: root = [4, 2, 7, 1, 3, 6, 9]
# Output: [4, 7, 2, 9, 6, 3, 1]
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(9)
inverted_root1 = Solution().invertTree(root1)
# The resulting tree should have the root value 4, left subtree [7, 9, 6], and right subtree [2, 3, 1]
print(inverted_root1.val)  # Output: 4
print(inverted_root1.left.val, inverted_root1.right.val)  # Output: 7, 2
print(
    inverted_root1.left.left.val,
    inverted_root1.left.right.val,
    inverted_root1.right.left.val,
)  # Output: 9, 6, 3
print(inverted_root1.right.right.val)  # Output: 1

# Example 2
# Input: root = [2, 1, 3]
# Output: [2, 3, 1]
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
inverted_root2 = Solution().invertTree(root2)
# The resulting tree should have the root value 2, left subtree [3, None, 1], and right subtree [1, None, 3]
print(inverted_root2.val)  # Output: 2
print(inverted_root2.left.val, inverted_root2.right.val)  # Output: 3, 1
print(
    inverted_root2.left.left, inverted_root2.left.right, inverted_root2.right.left
)  # Output: None, None, None
print(inverted_root2.right.right)  # Output: 3

# Example 3
# Input: root = []
# Output: []
root3 = None
inverted_root3 = Solution().invertTree(root3)
print(inverted_root3)  # Output: None
