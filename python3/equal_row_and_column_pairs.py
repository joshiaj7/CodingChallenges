from typing import List

"""
Space   : O(n^2)
Time    : O(n^2)
"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        h_row = {}
        h_col = {}

        # row
        for i in range(n):
            row = []
            for j in range(n):
                row.append(grid[i][j])
            
            tuprow = tuple(row)
            if tuprow in h_row:
                h_row[tuprow] += 1
            else:
                h_row[tuprow] = 1

        # col
        for i in range(n):
            row = []
            for j in range(n):
                row.append(grid[j][i])
            
            tuprow = tuple(row)
            if tuprow in h_col:
                h_col[tuprow] += 1
            else:
                h_col[tuprow] = 1

        for k, v in h_row.items():
            if k in h_col:
                ans += v * h_col[k]

        return ans
