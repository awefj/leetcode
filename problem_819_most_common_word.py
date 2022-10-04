import collections
import re


class Solution(object):
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        """
        :param paragraph: str
        :param banned: list[str]
        :return: str
        """
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        print(words)
        count = collections.Counter(words)
        return count.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
s = Solution()
print(s.mostCommonWord(paragraph, banned))
