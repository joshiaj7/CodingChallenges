"""
Space   : O(m * n * maxMove)
Time    : O(m * n * maxMove)
"""


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]

        def solve(x, y, move):
            if move < 0:
                return 0
            if y < 0 or y >= m or x < 0 or x >= n:
                return 1

            if dp[y][x][move] != -1:
                return dp[y][x][move]

            a = solve(x-1, y, move - 1)
            b = solve(x+1, y, move - 1)
            c = solve(x, y-1, move - 1)
            d = solve(x, y+1, move - 1)

            dp[y][x][move] = a + b + c + d
            return dp[y][x][move]

        return solve(startColumn, startRow, maxMove) % 1000000007
