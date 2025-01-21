from typing import List

"""
Space   : O(nm)
Time    : O(nm)
"""

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        ans = float('inf')
        n = len(grid)
        m = len(grid[0])

        prefsum = [[0 for _ in range(m)] for _ in range(n)]

        for left in range(m):
            right = m - left - 1

            if left == 0:
                prefsum[0][left] = grid[0][left]
                prefsum[1][right] = grid[1][right]
            else:
                prefsum[0][left] = grid[0][left] + prefsum[0][left-1] 
                prefsum[1][right] = grid[1][right] + prefsum[1][right+1] 

        totalTop = prefsum[0][-1]
        totalBot = prefsum[1][0]

        for i in range(m):
            remTop = totalTop - prefsum[0][i]
            remBot = totalBot - prefsum[1][i]

            ans = min(ans, max(remTop, remBot))

        return ans
