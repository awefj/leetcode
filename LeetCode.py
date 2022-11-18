# Definition for singly-linked list.
import collections
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_node_create(value_list: list) -> Optional[TreeNode]:
    if len(value_list) < 1:
        return None
    queue = collections.deque()
    index = 0
    root = TreeNode(value_list[index])
    queue.append(root)
    while queue:
        node = queue.popleft()
        if index + 1 < len(value_list):
            index += 1
            node_left = None
            if value_list[index] != "None":
                node_left = TreeNode(value_list[index])
                queue.append(node_left)
            node.left = node_left
        if index + 1 < len(value_list):
            index += 1
            node_right = None
            if value_list[index] != "None":
                node_right = TreeNode(value_list[index])
                queue.append(node_right)
            node.right = node_right
    return root


def tree_node_print(root: TreeNode) -> list:
    res = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            if node.left or node.right:
                queue.append(node.left)
                queue.append(node.right)
        else:
            res.append("None")
    return res
