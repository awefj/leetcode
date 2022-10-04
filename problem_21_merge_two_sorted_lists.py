from typing import Optional
from LeetCode import ListNode

class Solution:
    def mergeTwoLists00(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass


    def mergeTwoLists01(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists01(list1.next, list2)
        return list1

