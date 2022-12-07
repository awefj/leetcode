from typing import Optional

import LeetCode
from LeetCode import TreeNode


class Solution:
    max_val: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.left.val is node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val is node.val:
                right += 1
            else:
                right = 0

            self.max_val = max(self.max_val, left + right)
            return max(left, right)

        dfs(root)
        return self.max_val


list = "5, 4, 5, 1, 1, null, 5"
root = LeetCode.tree_node_create(list)
s = Solution()
print(s.longestUnivaluePath(root))
