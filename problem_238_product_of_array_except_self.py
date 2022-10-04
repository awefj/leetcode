class Solution(object):
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        pointer = 1
        for i in nums:
            res.append(pointer)
            pointer *= i
        pointer = 1
        for n, i in enumerate(nums[::-1]):
            res[-n-1] *= pointer
            pointer *= i

        return res


s = Solution()
nums = [1, 2, 3, 4]
print(s.productExceptSelf(nums))
