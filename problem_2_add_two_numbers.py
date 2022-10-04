from typing import Optional

from LeetCode import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, prev, rem = None, None, 0
        while l1 or l2 or rem > 0:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            rem, val = divmod(sum + rem, 10)
            node = ListNode(val)
            if head is None:
                head = prev = node
            else:
                prev.next = node
            rem = int((val + rem) / 10)
            prev = node
        return head

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    def to_list(self, node: Optional[ListNode]) -> Optional[list]:
        list_val: list = []
        while node:
            list_val.append(node.val)
            node = node.next
        return list_val

    def to_reversed_linked_list(self, result: Optional[str]) -> Optional[ListNode]:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    # 자료형 변환
    def add_two_numbers_01(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.to_list(self.reverse_list(l1))
        b = self.to_list(self.reverse_list(l2))
        result = int(''.join(str(e) for e in a)) + \
                 int(''.join(str(e) for e in b))
        return self.to_reversed_linked_list(str(result))

    # 전가산기 구현
    def add_two_numbers_02(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        return root.next


l1 = ListNode(9)
l1.next = ListNode(9)
l2 = ListNode(9)
l2.next = ListNode(8)
sol = Solution()
res = sol.add_two_numbers_01(l1, l2)
while res:
    print(res.val, end='')
    res = res.next
print()
