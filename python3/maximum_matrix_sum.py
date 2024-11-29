from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        n = len(matrix)
        neg = 0
        minVal = float('inf')

        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    neg += 1
                ans += abs(matrix[i][j])
                minVal = min(minVal, abs(matrix[i][j]))

        if neg % 2 == 1:
            ans -= 2 * minVal

        return ans
        