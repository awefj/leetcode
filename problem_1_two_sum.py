class Solution(object):
    def twoSum00(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum01(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(diff) + i + 1]

    def twoSum02(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, num in enumerate(nums):
            map[num] = i
        for i, num in enumerate(nums):
            if target - num in map and i != map[target - num]:
                return [i, map[target - num]]

    def twoSum03(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, num in enumerate(nums):
            if target - num in map:
                return [map[target - num], i]
            map[num] = i


s = Solution()
nums = [2, 7, 11, 15]
print(s.twoSum00(nums, 9))
print(s.twoSum01(nums, 9))
print(s.twoSum02(nums, 9))
print(s.twoSum03(nums, 9))
