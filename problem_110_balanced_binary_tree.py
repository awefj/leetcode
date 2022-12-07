from typing import Optional

import LeetCode
from LeetCode import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        heights = []

        def get_height(cur: int, node: TreeNode):
            if node is None:
                heights.append(cur)
                return
            get_height(cur + 1, node.left)
            get_height(cur + 1, node.right)

        if root is None:
            return True
        get_height(0, root)
        max_val, min_val = max(heights), min(heights)
        if max_val - min_val > 1:
            return False
        return True

    def isBalanced01(self, root: Optional[TreeNode]) -> bool:
        def check(root: Optional[TreeNode]):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(root) != -1


root1 = LeetCode.tree_node_create('1,2,3,4,5,6,null,8')

s = Solution()
print(s.isBalanced(root1))
print(s.isBalanced01(root1))
