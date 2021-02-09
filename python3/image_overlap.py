from collections import Counter

"""
Space   : O(n)
Time    : O(n**2)
"""

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        A_grid, B_grid = [], []

        for i, row in enumerate(A):
            for j, item in enumerate(row):
                if item:
                    A_grid.append((i, j))

        for i, row in enumerate(B):
            for j, item in enumerate(row):
                if item:
                    B_grid.append((i, j))

        res = []
        for ax, ay in A_grid:
            for bx, by in B_grid:
                res.append((ax-bx, ay-by))

        return max(Counter(res).values() or [0])
