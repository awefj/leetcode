class Solution:
    def isValid(self, s: str) -> bool:
        left = "({["
        right = ")}]"
        list = []
        for p in s:
            if p in left:
                list.append(p)
            elif p in right:
                if len(list) < 1:
                    return False
                if left.index(list.pop()) != right.index(p):
                    return False
        if len(list) == 0:
            return True
        return False


input: str = "(()))"
sol = Solution()
print(sol.isValid(input))
