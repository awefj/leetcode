from typing import List


class Solution:
    def subsets01(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx, path):
            res.append(path)
            for i in range(idx, len(nums)):
                dfs(i + 1, path + [nums[i]])

        res = []
        dfs(0, [])
        return res
