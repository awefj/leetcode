import sys


class Solution(object):
    def maxProfit(self, prices: list[int]) -> int:
        min_val, res = sys.maxsize, 0
        for val in prices:
            min_val = min(min_val, val)
            res = max(res, val - min_val)
        return res

s = Solution()
# prices = [7, 1, 5, 3, 6, 4]
prices = [1,2,4,2,5,7,2,4,9,0,9]
print(s.maxProfit(prices))
