import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st: list = list(s)
        a_val: int = ord("a")
        last_loc: list = [-1] * (ord("z") - a_val + 1)
        for i in range(len(st)):
            alphabet_num = ord(st[i])-a_val
            if last_loc[alphabet_num] > -1:
                st[last_loc[alphabet_num]] = " "
            last_loc[alphabet_num] = i
        return ''.join(st).replace(" ", "")

    def removeDuplicateLetters01(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char,''))
        return ''

    def removeDuplicateLetters02(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        for char in s:
            counter[char] -=1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]]>0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)

    def removeDuplicateLetters03(self, s:str)->str:
        counter, stack = collections.Counter(s), []
        for char in s:
            counter[char]-=1
            if char in stack:
                continue
            while stack and char < stack[-1] and counter[stack[-1]]>0:
                stack.pop()
            stack.append(char)
        return ''.join(stack)

input = "cbacdcbc"
sol = Solution()
print(sol.removeDuplicateLetters03(input))
