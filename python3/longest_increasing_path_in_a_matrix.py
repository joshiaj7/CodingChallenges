"""
Space   : O(mn)
Time    : O(mn)

Method:
Dynamic Programming - DFS
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(x, y):
            if not dp[y][x]:
                val = matrix[y][x]
                dp[y][x] = 1 + max(
                    dfs(x, y - 1) if y > 0 and val > matrix[y-1][x] else 0,
                    dfs(x, y + 1) if y < (row -
                                          1) and val > matrix[y + 1][x] else 0,
                    dfs(x - 1, y) if x > 0 and val > matrix[y][x - 1] else 0,
                    dfs(x + 1, y) if x < (col -
                                          1) and val > matrix[y][x + 1] else 0,
                )
            return dp[y][x]

        if not matrix or not matrix[0]:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * col for _ in range(row)]
        return max(dfs(x, y) for x in range(col) for y in range(row))
