"""
Space   : O(n^2)
Time    : O(n^2)
"""

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ones = []
        m, n = len(grid), len(grid[0])
        coord = [(0,1), (1,0), (0,-1), (-1,0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones.append((i, j))

        if len(ones) == 0 or len(ones) == m*n:
            return -1

        ans = 0
        while ones:
            temp = []
            for i, j in ones:
                for dx, dy in coord:
                    nx = dx + i
                    ny = dy + j
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        temp.append((nx, ny))
            ans += 1
            ones = temp

        return ans - 1
