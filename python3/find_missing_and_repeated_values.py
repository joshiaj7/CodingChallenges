from typing import List

"""
Space   : O(n^2)
Time    : O(n^2)
"""


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0, 0]
        n = len(grid)

        h = {}
        total = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] in h:
                    ans[0] = grid[i][j]
                else:
                    h[grid[i][j]] = 1
                    total += grid[i][j]
        
        trueSum = 0
        for i in range(1, (n**2)+1):
            trueSum += i

        ans[1] = trueSum - total
        return ans
        