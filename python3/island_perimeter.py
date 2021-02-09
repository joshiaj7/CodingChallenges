# leetcode

class Solution:
    def checkTop(self, x, y, grid):
        if grid[y-1][x] == 0:
            return 1
        else:
            return 0
        
    def checkBot(self, x, y, grid):
        if grid[y+1][x] == 0:
            return 1
        else:
            return 0
        
    def checkRight(self, x, y, grid):
        if grid[y][x+1] == 0:
            return 1
        else:
            return 0
        
    def checkLeft(self, x, y, grid):
        if grid[y][x-1] == 0:
            return 1
        else:
            return 0
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0 
        len_y = len(grid)
        len_x = len(grid[0])
        
        for y in range(len_y):
            for x in range(len_x):
                if grid[y][x] == 1:
                    if (x == 0 and x == len_x - 1):
                        ans += 2
                    elif x == 0:  
                        ans += 1
                        ans += self.checkRight(x, y, grid)
                    elif x == len_x - 1:
                        ans += 1
                        ans += self.checkLeft(x, y, grid)
                    else:
                        ans += self.checkRight(x, y, grid)
                        ans += self.checkLeft(x, y, grid)
                        
                    if (y == 0 and y == len_y - 1):
                        ans += 2
                    elif y == 0:
                        ans += 1
                        ans += self.checkBot(x, y, grid)
                    elif y == len_y - 1:
                        ans += 1
                        ans += self.checkTop(x, y, grid)
                    else:
                        ans += self.checkBot(x, y, grid)
                        ans += self.checkTop(x, y, grid)

        return ans
        