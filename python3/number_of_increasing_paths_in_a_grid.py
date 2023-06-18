from typing import List

"""
Space   : O(nm)
Time    : O((nm)^2 * log nm )

Method:
DP
"""

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n, mod = len(grid), len(grid[0]), 10 ** 9 + 7
        dp = [[1] * n for i in range(m)]

        coords = []
        for i in range(m):
            for j in range(n):
                coords.append([grid[i][j], i, j])
        coords = sorted(coords)

        dcoords = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for val, i, j in coords:
            for dx, dy in dcoords:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] < val:
                    dp[i][j] += dp[nx][ny] % mod

        ans = 0
        for x in dp:
            ans += sum(x) % mod

        return ans % mod
