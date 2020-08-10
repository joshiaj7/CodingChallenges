# leetcode

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        if (row == 1 and col == 1) and obstacleGrid[row-1][col-1] == 1:
            return 0
        if obstacleGrid[row-1][col-1] == 1:
            return 0
        
        # change obs to -1
        for y in range(row):
            for x in range(col):
                if obstacleGrid[y][x] == 1:
                    obstacleGrid[y][x] = -1
                    
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        obstacleGrid[i][j] = 1
                    elif i == 0:
                        left = obstacleGrid[i][j-1] if obstacleGrid[i][j-1] != -1 else 0
                        obstacleGrid[i][j] = left
                    elif j == 0:
                        top = obstacleGrid[i-1][j] if obstacleGrid[i-1][j] != -1 else 0
                        obstacleGrid[i][j] = top
                    else:
                        top = obstacleGrid[i-1][j]
                        left = obstacleGrid[i][j-1]
                        if top == -1:
                            top = 0 
                        if left == -1:
                            left = 0
                        obstacleGrid[i][j] = top + left
        
        print(obstacleGrid)
        return obstacleGrid[row-1][col-1] if obstacleGrid[row-1][col-1] != -1 else 0