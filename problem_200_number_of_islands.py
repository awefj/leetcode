from typing import List


class Solution:
    def flood_fill(self, grid: List[List[str]], i: int, j: int, val: int):
        # check range
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == '1':
                grid[i][j] = str(int)
                self.flood_fill(grid, i - 1, j, val)
                self.flood_fill(grid, i, j - 1, val)
                self.flood_fill(grid, i + 1, j, val)
                self.flood_fill(grid, i, j + 1, val)

    def numIslands(self, grid: List[List[str]]) -> int:
        val = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.flood_fill(grid, i, j, val)
                    val += 1
        return val - 1


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
s = Solution()
print(s.numIslands(grid))
