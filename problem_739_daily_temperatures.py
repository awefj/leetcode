from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, answer = [], [0] * len(temperatures)
        for index, current in enumerate(temperatures):
            while stack and current > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = index - last
            stack.append(index)
        return answer

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer
