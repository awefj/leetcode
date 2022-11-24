import collections
from typing import Optional

import LeetCode
from LeetCode import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursive way
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

    def invertTree01(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # using bfs
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

    def invertTree02(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # using dfs with preorder traversal
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root

    def invertTree03(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # using dfs with postorder traversal
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                node.left, node.right = node.right, node.left
        return root


root = LeetCode.tree_node_create([1, 2, 3, 4, 5, 6, 7])
print(root.val, root.left.val, root.right.val)
s = Solution()
new_root = s.invertTree(root)
print(LeetCode.tree_node_print(new_root))
