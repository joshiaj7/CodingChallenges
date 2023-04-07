"""
Space   : O(1)
Time    : O(mn)
"""

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        coord = [(1,0), (0,1), (-1, 0), (0, -1)]

        def dfs(i, j, m, n, value):
            grid[i][j] = value

            if value == 0:
                self.ans += 1

            for di, dj in coord:
                new_i = i + di
                new_j = j + dj

                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1:
                    dfs(new_i, new_j, m, n, value)

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 1:
                    dfs(i, j, m, n, -1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 1

        return ans
