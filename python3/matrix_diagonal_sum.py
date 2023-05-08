"""
Space   : O(1)
Time    : O(n^2)
"""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)

        for i in range(n):
            for j in range(n):
                if i - j == 0 or i + j == n - 1:
                    ans += mat[i][j]
                
        return ans
    