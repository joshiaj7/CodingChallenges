"""
space : O(mn)
time  : O(mn)
"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        ans = []
        
        for x in range(col):
            line = []
            for y in range(row):
                line.append(matrix[y][x]) 
            ans.append(line)
        
        return ans
