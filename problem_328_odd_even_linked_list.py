from typing import Optional
from LeetCode import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = odd_prev = ListNode(1)
        even = even_prev = ListNode(2)
        counter = 0
        while head:
            if counter % 2 == 0:  # even
                odd_prev.next = head
                odd_prev = head
            else:  # odd
                even_prev.next = head
                even_prev = head
            head = head.next
            counter += 1
        # combine odd and even linked lists
        even_prev.next = None
        odd_prev.next = even.next
        return odd.next


input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
ret = sol.oddEvenList(input)
while ret:
    print(ret.val, end="")
    ret = ret.next
print()
