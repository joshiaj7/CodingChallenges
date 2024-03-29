"""
Space   : O(1)
Time    : O(4^(m*n))
"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        m, n = len(grid), len(grid[0])
        x, y = 0, 0
        empty = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = (i, j)
                elif grid[i][j] == 0:
                    empty += 1

        def dfs(x, y, empty):
            if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0):
                return
            if grid[x][y] == 2:
                if empty == 0:
                    self.ans += 1
                return
            
            grid[x][y] = -2
            dfs(x - 1, y, empty - 1)
            dfs(x + 1, y, empty - 1)
            dfs(x, y - 1, empty - 1)
            dfs(x, y + 1, empty - 1)
            grid[x][y] = 0 

        dfs(x, y, empty)
        return self.ans
