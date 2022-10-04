from typing import Optional
import collections
from LeetCode import ListNode

class Solution:
    def isPalindrome00(self, head: Optional[ListNode]) -> bool:
        items = []
        if not head:
            return True
        while head:
            items.append(head.val)
            head = head.next
        return items == items[::-1]

    def isPalindrome01(self, head: Optional[ListNode]) -> bool:
        items = collections.deque()
        if not head:
            return True
        node = head
        while node is not None:
            items.append(node.val)
            node = node.next
        while len(items) > 1:
            if items.popleft() != items.pop():
                return False
        return True

    def isPalindrome02(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
