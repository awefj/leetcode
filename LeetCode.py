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
    index += 1
    while queue:
        node = queue.popleft()
        if index < len(value_list) and value_list[index]:
            node.left = TreeNode(int(value_list[index]))
            queue.append(node.left)
        index += 1
        if index < len(value_list) and value_list[index]:
            node.right = TreeNode(int(value_list[index]))
            queue.append(node.right)
        index += 1

    return root


def tree_node_print(root: TreeNode) -> list:
    res = []
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)

    # remove useless "None"s
    res = res[::-1]
    while len(res) > 0:
        if res[0]:
            break
        else:
            del res[0]
    return res[::-1]
