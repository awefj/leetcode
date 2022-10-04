from typing import Optional
from LeetCode import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(0)
        while head and head.next:
            front, back = head, head.next
            target = back.next
            prev.next, back.next = back, front
            front.next, prev = target, front
            head = target
        prev.next = head
        return root.next
