import collections
import re


class Solution(object):
    def isPalindrome_00(self, s) -> bool:
        """
        :param s: str
        :return: bool
        """
        # clean input
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        # check palindrome
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

    def isPalindrome_01(self, s) -> bool:
        """
        :param s:
        :return:
        """
        # clean input
        strs = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

    def isPalindrome_02(self, s) -> bool:
        """
        :param s:
        :return:
        """
        # clean input
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        # check palindrome
        return s == s[::-1]

s = Solution()