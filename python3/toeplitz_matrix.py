"""
Space   : O(1)
Time    : O(mn)
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) == 0:
            return True
        if len(matrix[0]) == 0:
            return True

        ly = len(matrix)
        lx = len(matrix[0])

        for y in range(ly-1):
            for x in range(lx-1):
                if matrix[y][x] != matrix[y+1][x+1]:
                    return False

        return True
