import collections
from typing import Optional

import LeetCode
from LeetCode import TreeNode


class Codec:

    def my_serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        return LeetCode.tree_node_print(root)

    def my_deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        return LeetCode.tree_node_create(data)

    def serialize(self, root: Optional[TreeNode]) -> Optional[str]:
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = [None]
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)
        return ' '.join(map(str, res))

    def deserialize(self, data: Optional[str]) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == 'None None':
            return None
        value_list = data.split()
        queue = collections.deque()
        index = 1
        root = TreeNode(value_list[index])
        queue.append(root)
        index += 1
        while queue:
            node = queue.popleft()
            if value_list[index] != 'None':
                node.left = TreeNode(int(value_list[index]))
                queue.append(node.left)
            index += 1
            if value_list[index] != 'None':
                node.right = TreeNode(int(value_list[index]))
                queue.append(node.right)
            index += 1
        return root


class Codec01:
    # 직렬화
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ['#']
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    # 역직렬화
    def deserialize(self, data: str) -> TreeNode:
        # 예외 처리
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        # 빠른 런너처럼 자식 노드 결과 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] != '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
null = None
str1 = ''
str2 = '5, 4, 7, 3, null, 2, null, -1, null, 9'
root1 = LeetCode.tree_node_create(str1)
root2 = LeetCode.tree_node_create(str2)
ser = Codec01()
deser = Codec01()
codec01_line1 = ser.serialize(root1)
codec01_line2 = ser.serialize(root2)
print("codec01")
print(codec01_line1)
print(codec01_line2)
print("codec")
co_ser = Codec()
co_deser = Codec()
codec_myline1 = co_ser.my_serialize(root1)
codec_myline2 = co_ser.my_serialize(root2)
print("my_serialize & my_deserialize")
print(codec_myline1)
print(codec_myline2)
codec_line1 = co_ser.serialize(root1)
codec_line2 = co_ser.serialize(root2)
print("serialize & deserialize")
print(codec_line1)
print(codec_line2)
