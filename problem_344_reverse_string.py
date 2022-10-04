class Solution(object):
    def reverseString_00(self, s: list[str]) -> None:
        """
        :param s:
        :return: None
        """
        for i in range(len(s) // 2):
            front = s[i]
            s[i] = s[-1 - i]
            s[-1 - i] = front

    def reverseString_01(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseString_02(self, s: list[str]) -> None:
        s.reverse()

    def reverseString_03(self, s: list[str]) -> None:
        s[:] = s[::-1]
