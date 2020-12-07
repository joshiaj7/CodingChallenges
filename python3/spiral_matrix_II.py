# Space : O(n**2)
# Time  : O(n**2)

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        
        matrix = [[0] * n for i in range(n)]

        count = 2
        x, y = 1, 0
        direction = 'x+'
        matrix[0][0] = 1
        
        def updateCoor(x, y, direction):
            if direction == 'x+':
                return x + 1, y
            elif direction == 'x-':
                return x - 1, y
            elif direction == 'y+':
                return x, y + 1
            else:
                return x, y - 1
        
        
        while count <= n*n:
            # update matrix and direction
            if direction == 'x+':
                matrix[y][x] = matrix[y][x-1] + 1
                if x == len(matrix[0])-1 or matrix[y][x+1] > 0:
                    direction = 'y+'
                    
            elif direction == 'x-':
                matrix[y][x] = matrix[y][x+1] + 1
                if x == 0 or matrix[y][x-1] > 0:
                    direction = 'y-'
                
            elif direction == 'y+':
                matrix[y][x] = matrix[y-1][x] + 1
                if y == len(matrix)-1 or matrix[y+1][x] > 0:
                    direction = 'x-'
                
            elif direction == 'y-':
                matrix[y][x] = matrix[y+1][x] + 1
                if y == 0 or matrix[y-1][x] > 0:
                    direction = 'x+'
            
            # update coordinate
            count += 1
            x, y = updateCoor(x, y, direction)
        
        return matrix