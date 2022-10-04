class Solution(object):
    def arrayPairSum00(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        for i in nums[::2]:
            res += i
        return res

    def arrayPairSum01(self, nums: list[int]) -> int:
        sum = 0
        pair = []
        nums.sort()
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum

    def arrayPairSum02(self, nums: list[int]) -> int:
        sum = 0
        nums.sort()
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        return sum

    def arrayPairSum03(self, nums: list[int]) -> int:
        return (sum(sorted(nums)[::2]))


s = Solution()
nums = [6, 2, 6, 5, 1, 2]
print(s.arrayPairSum00(nums))
print(s.arrayPairSum01(nums))
print(s.arrayPairSum02(nums))
print(s.arrayPairSum03(nums))
