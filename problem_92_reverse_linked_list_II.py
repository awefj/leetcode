from typing import Optional
from LeetCode import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = root = head
        front = back = prev = None
        counter = 1
        if not head or left == right:
            return head
        while node:
            if left <= counter <= right:
                if left == counter:
                    front, back = prev, node
                next_node, node.next = node.next, prev
                if right == counter:
                    if front:
                        front.next, back.next = node, next_node
                        return head
                    else:
                        head, back.next = node, next_node
                        return head
                prev, node = node, next_node
            else:
                prev, node = node, node.next
            counter += 1
        return head

    def reverseBetween01(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        root = start = ListNode(0)
        root.next = head
        for _ in range(left-1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next


input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
res = sol.reverseBetween(input, 1, 5)
while res:
    print(res.val, end="")
    res = res.next
print()
