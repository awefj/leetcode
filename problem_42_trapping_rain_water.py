class Solution(object):
    def trap00(self, height: list[int]) -> int:
        max, min, cnt, tmp, res = 0, 0, 0, 0, 0
        for val in height:
            # print(f"val : {val} ", end="")
            if max > val:
                if min > val:
                    min = val
                    tmp += max - val
                    cnt += 1
                else:
                    tmp += max - val
                    cnt += 1
                # print(f"tmp : {tmp}")
            else:
                res += tmp
                max = min = val
                cnt, tmp = 0, 0
                # print(f"tmp : {tmp}, res : {res}")
        return res

    def trap01(self, height: list[int]) -> int:
        if not height:
            return 0
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

    def trap02(self, height: list[int])->int:
        stack=[]
        vol = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break
                distance = i - stack[-1] -1
                water = min(height[i], height[stack[-1]])-height[top]
                vol += distance * water
            stack.append(i)
        return vol

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 2]
s = Solution()
print(s.trap00(height))
print(s.trap01(height))
print(s.trap02(height))
