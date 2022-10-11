from typing import List


class Solution:
    def letterCombinations01(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                res.append(path)
                return
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        dic = {"2": "abc", "3": "def",
               "4": "ghi", "5": "jkl", "6": "nmo",
               "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        if digits:
            dfs(0, "")
        return res


s = Solution()
print(s.letterCombinations01("23"))
