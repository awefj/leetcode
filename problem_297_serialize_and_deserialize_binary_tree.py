import collections

import LeetCode
from LeetCode import TreeNode


class Codec:

    def my_serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return ','.join(LeetCode.tree_node_print(root))

    def my_deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        list_data = data.split(sep=",")
        return LeetCode.tree_node_create(list_data)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = collections.deque()
        queue.append(root)

        # create list from root
        while queue:
            node = queue.popleft()
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')

        # remove useless 'null'
        res = res[::-1]
        while len(res) > 0:
            if res[0] == 'null':
                del res[0]
            else:
                break

        # return result list as string separated by ','
        return ','.join(map(str,res[::-1]))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # create list from data
        list_data = data.split(sep=",")

        if len(list_data) < 1:
            return None

        queue = collections.deque()
        idx = 0
        root = TreeNode(list_data[idx])
        queue.append(root)
        while queue:
            node = queue.popleft()
            if idx + 1 < len(list_data):
                idx += 1
                node_left = None
                if list_data[idx] != 'null':
                    node_left = TreeNode(list_data[idx])
                    queue.append(node_left)
                node.left = node_left
            if idx + 1 < len(list_data):
                idx += 1
                node_right = None
                if list_data[idx] != 'null':
                    node_right = TreeNode(list_data[idx])
                    queue.append(node_right)
                node.right = node_right
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

line = "1,2,3,null,null,4,5"
c = Codec()
root = c.deserialize(line)
print(c.serialize(root))
