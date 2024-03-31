class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        # Check if the current node is a leaf node
        if not root.left and not root.right:
            # If the current node is a leaf, check if its value matches the target sum
            return targetSum == root.val
        
        # Subtract the current node's value from the target sum
        targetSum -= root.val
        
        # Recursively check if there's a path with the updated target sum in the left or right subtree
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# Runtime 39 ms / Memory 17.48 mb
