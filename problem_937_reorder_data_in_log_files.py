class Solution(object):
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        """
        :param logs: list[str]
        :return: list[str]
        """
        char, digit = [], []
        for item in logs:
            if item.split()[1].isdigit():
                digit.append(item)
            else:
                char.append(item)
        char.sort(key=lambda char: (char.split()[1:], char.split()[0]))
        return char + digit


s = Solution()
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(s.reorderLogFiles(logs))
