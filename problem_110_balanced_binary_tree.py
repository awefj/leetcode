from typing import Optional

import LeetCode
from LeetCode import TreeNode


class Solution:
    heights = []

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(cur: int, node: TreeNode):
            if node is None:
                self.heights.append(cur)
                return
            get_height(cur + 1, node.left)
            get_height(cur + 1, node.right)

        if root is None:
            return True
        get_height(0, root)
        self.heights.sort()
        if self.heights[-1] - self.heights[0] > 1:
            return False
        return True

root = LeetCode.tree_node_create([1])
print(LeetCode.tree_node_print(root))
s=Solution()
print(s.isBalanced(root))