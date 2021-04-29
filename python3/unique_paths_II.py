# Space : O(1) 
# Time  : O(n*m)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
            
        obstacleGrid[0][0] = -1
        
        for y in range(row):
            for x in range(col):
                if obstacleGrid[y][x] != 1:
                    if 0 < y < row and obstacleGrid[y-1][x] < 0:
                        obstacleGrid[y][x] += obstacleGrid[y-1][x]
                    if 0 < x < col and obstacleGrid[y][x-1] < 0:
                        obstacleGrid[y][x] += obstacleGrid[y][x-1]
        
        return -obstacleGrid[-1][-1] if obstacleGrid[-1][-1] != 1 else 0