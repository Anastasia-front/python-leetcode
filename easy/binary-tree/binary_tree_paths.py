from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, path):
            # If the node is None, return
            if not node:
                return

            # Add the current node to the path
            path.append(str(node.val))

            # If it's a leaf node, add the path to the result
            if not node.left and not node.right:
                paths.append("->".join(path))
                return

            # Recursively traverse left and right subtrees
            dfs(node.left, path[:])
            dfs(node.right, path[:])

        paths = []
        dfs(root, [])
        return paths


# Runtime 34 ms / Memory 16.59 mb


# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
print(Solution().binaryTreePaths(root1))  # Output: ["1->2->5", "1->3"]

# Example 2
root2 = TreeNode(1)
print(Solution().binaryTreePaths(root2))  # Output: ["1"]
