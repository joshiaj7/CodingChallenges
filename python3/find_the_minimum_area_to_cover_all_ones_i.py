from typing import List

"""
Space   : O(1)
Time    : O(nm)
"""

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        left, right = n, -1
        top, bottom = m, -1

        oneExist = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    oneExist = True
                    left = min(left, j)
                    right = max(right, j)
                    top = min(top, i)
                    bottom = max(bottom, i)

        if not oneExist:
            return 0

        return (right - left + 1) * (bottom - top + 1)
