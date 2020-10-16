"""
Space   : O(1)
Time    : O(m+n)
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)

        if row == 0:
            return False

        col = len(matrix[0])

        if col == 0:
            return False

        x, y = col-1, row-1

        while x >= 0:
            if matrix[y][x] == target:
                return True
            else:
                if y > 0 and matrix[y-1][x] >= target:
                    y -= 1
                elif x > 0 and matrix[y][x-1] >= target:
                    x -= 1
                else:
                    break

        return False
