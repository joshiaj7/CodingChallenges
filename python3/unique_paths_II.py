"""
Space : O(1) 
Time  : O(n*m)

Method:
Dynamic Programming (DP)
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        dp = [[0] * col for _ in range(row)]

        for y in range(row):
            for x in range(col):
                if obstacleGrid[y][x] == 1:
                    continue

                if y == 0 and x == 0:
                    dp[y][x] = 1
                elif y == 0:
                    dp[y][x] = dp[y][x-1]
                elif x == 0:
                    dp[y][x] = dp[y-1][x]
                else:
                    dp[y][x] = dp[y][x-1] + dp[y-1][x]

        return dp[-1][-1]
