class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)


s = Solution()
jew = "aA"
sto = "aAAbbbb"
print(s.numJewelsInStones(jew,sto))
