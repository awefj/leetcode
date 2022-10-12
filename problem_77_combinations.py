import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        target = list(range(1, n + 1))
        return list(map(list, itertools.combinations(target, k)))

    def combine01(self, n: int, k: int) -> List[List[int]]:
        def dfs(val: int):
            prev.append(val)
            if len(prev) == k:
                res.append(prev[:])
                prev.pop()
                return
            for j in range(val + 1, n + 1):
                dfs(j)
            prev.pop()

        res = []
        prev = []
        for i in range(1, n + 1):
            dfs(i)
        return res


s = Solution()
print(s.combine(6, 4))
print(s.combine01(6, 4))
