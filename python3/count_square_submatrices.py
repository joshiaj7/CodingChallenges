# leetcode

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        ans = 0
        
        for y in range(row):
            for x in range(col):
                if y > 0 and x > 0:
                    if (matrix[y][x-1] > 0) and (matrix[y-1][x-1] > 0) and (matrix[y-1][x] > 0) and (matrix[y][x] > 0):
                        matrix[y][x] = min(matrix[y][x-1], matrix[y-1][x-1], matrix[y-1][x]) + 1
                        # matrix[y][x] += 1
                ans += matrix[y][x]
                    
                
        for i in matrix:
            print(i)
        # print(min(1,2,3))      
        print(ans)
        return ans
                        
        