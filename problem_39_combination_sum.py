from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(ind: int):
            prev.append(candidates[ind])
            if sum(prev) == target:
                res.append(prev[:])
                prev.pop()
                return
            for i in range(ind, len(candidates)):
                if sum(prev) + candidates[i] <= target:
                    dfs(i)
            prev.pop()

        res = []
        prev = []
        for i in range(len(candidates)):
            dfs(i)
        return res


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
