"""
Space   : O(1)
Time    : O(nm)
"""


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        coord = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        if n == 1 or m == 1:
            return 0
                    
        # invalidate grid edges
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n-1 or j == m-1) and grid[i][j] == 0:
                    grid[i][j] = -1
                    

        def dfs(i, j, n, m, value):
            grid[i][j] = value
            for di, dj in coord:
                ni = i + di
                nj = j + dj

                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 0:
                    dfs(ni, nj, n, m, value)

        # invalidate neighbor cells
        for i in range(n):
            for j in range(m):
                if grid[i][j] == -1:
                    dfs(i, j, n, m, -1)

        # calculate answer
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i, j, n, m, 1)
                    ans += 1

        return ans
