"""
Space : O(1) 
Time  : O(n*m)

Method:
Dynamic Programming (DP)
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] != 1:
                    continue

                if i == 0 and j == 0:
                    obstacleGrid[i][j] = -1
                elif i == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else:
                    if obstacleGrid[i][j-1] != 1:
                        obstacleGrid[i][j] += obstacleGrid[i][j-1] 
                    if obstacleGrid[i-1][j] != 1:
                        obstacleGrid[i][j] += obstacleGrid[i-1][j] 

        return -obstacleGrid[-1][-1] if obstacleGrid[-1][-1] != 1 else 0

