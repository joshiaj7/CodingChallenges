from typing import List
from collections import defaultdict

"""
Space   : O(nm)
Time    : O(nm)
"""

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])
        rows = defaultdict(int)
        cols = defaultdict(int)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                    ans += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    ans -= 1

        return ans
