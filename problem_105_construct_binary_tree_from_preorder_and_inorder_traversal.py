import collections
from typing import List, Optional

from LeetCode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) > 0 and len(inorder) > 0:
            root: TreeNode = TreeNode(preorder[0])
            separator = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:separator + 1], inorder[0:separator])
            root.right = self.buildTree(preorder[separator + 1:], inorder[separator + 1:])
            return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
s = Solution()
root = s.buildTree(preorder, inorder)
queue = collections.deque()
queue.append(root)
while queue:
    node = queue.popleft()
    if node:
        print(node.val)
        queue.append(node.left)
        queue.append(node.right)
