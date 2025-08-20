from typing import List

"""
Space   : O(1)
Time    : O(mn)
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                elif matrix[i][j] > 0:
                    if matrix[i-1][j-1] > 0 and matrix[i-1][j] > 0 and matrix[i][j-1] > 0:
                        matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1

        for i in range(m):
            ans += sum(matrix[i])

        return ans
        