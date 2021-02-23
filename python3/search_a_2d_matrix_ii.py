# Space : O(1) 
# Time  : O(m + n)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        y, x = row-1, 0
        
        while y >= 0 and x < col:
            if matrix[y][x] == target:
                return True
            
            if matrix[y][x] < target:
                x += 1
            else:
                y -= 1
        
        return False