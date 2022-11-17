from typing import Optional

from LeetCode import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root


root = TreeNode(2, TreeNode(1), TreeNode(3))
print(root.val, root.left.val, root.right.val)
s = Solution()
new_root = s.invertTree(root)
print(new_root.val, new_root.left.val, new_root.right.val)
