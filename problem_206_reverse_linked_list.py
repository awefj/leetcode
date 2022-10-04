from typing import Optional
from LeetCode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        a, b, c = None, head, head.next
        while c:
            d = c.next
            b.next, c.next = a, b
            a, b, c = b, c, d
        return b

    def reverseList01(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: Optional[ListNode]):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

    def reverseList02(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
