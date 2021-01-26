"""
Space   : O(1)
Time    : O(nm)
"""


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        row = len(A)
        col = len(A[0])

        if row == 1:
            return min(A[0])
        if col == 1:
            ans = 0
            for i in range(row):
                ans += A[i][0]
            return ans

        for y in range(1, row):
            for x in range(col):
                if x == 0:
                    A[y][x] += min(A[y-1][x], A[y-1][x+1])
                elif x == col-1:
                    A[y][x] += min(A[y-1][x], A[y-1][x-1])
                else:
                    A[y][x] += min(A[y-1][x-1], A[y-1][x], A[y-1][x+1])

        return min(A[-1])
