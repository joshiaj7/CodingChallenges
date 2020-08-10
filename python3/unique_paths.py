# leetcode

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for i in range(n):
            grid.append([0]*m)
        
        for row in range(n):
            for col in range(m):
                if row == 0:
                    grid[row][col] = 1
                elif col == 0:
                    grid[row][col] = 1
                else:
                    grid[row][col] = grid[row-1][col] + grid[row][col-1]

        for x in grid:
            print(x)
            
        return grid[n-1][m-1]