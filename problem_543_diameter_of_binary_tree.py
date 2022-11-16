import collections
from typing import Optional
from LeetCode import TreeNode


class Solution:
    max_val: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            self.max_val = max(self.max_val, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.max_val
