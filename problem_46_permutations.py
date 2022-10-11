import itertools
from typing import List


class Solution:
    def permute01(self, nums: List[int]) -> List[List[int]]:
        def dfs(elem):
            if len(elem) == 0:
                res.append(prev_elem[:])
            for e in elem:
                next_elem = elem[:]
                next_elem.remove(e)
                prev_elem.append(e)
                dfs(next_elem)
                prev_elem.pop()

        res = []
        prev_elem = []
        dfs(nums)
        return res

    def permute02(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))


s = Solution()
print(s.permute01([1, 2, 4]))
print(s.permute02([1, 2, 4]))
