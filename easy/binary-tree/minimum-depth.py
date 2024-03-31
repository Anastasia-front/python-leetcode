class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        # If the node has no left child, we calculate the depth of the right subtree
        if not root.left:
            return self.minDepth(root.right) + 1

        # If the node has no right child, we calculate the depth of the left subtree
        if not root.right:
            return self.minDepth(root.left) + 1

        # If the node has both left and right children, we calculate the minimum depth of both subtrees
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# Runtime 234 ms / Memory 43.29 mb
