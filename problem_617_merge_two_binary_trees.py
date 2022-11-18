from typing import Optional

import LeetCode
from LeetCode import TreeNode


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            return TreeNode(
                root1.val + root2.val,
                self.mergeTrees(root1.left, root2.left),
                self.mergeTrees(root1.right, root2.right)
            )
        else:
            return root1 or root2


root1 = LeetCode.tree_node_create([1, 3, 2, 5, 'None'])
root2 = LeetCode.tree_node_create([2, 1, 3, 'None', 4, 'None', 7])
s = Solution()
node = s.mergeTrees(root1, root2)
print(LeetCode.tree_node_print(node))
