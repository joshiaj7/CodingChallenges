from typing import List
from collections import defaultdict

"""
Space   : O(nm)
Time    : O(k)
k = len(arr)
"""

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        coord = defaultdict(dict)
        row = defaultdict(int)
        col = defaultdict(int)

        n = len(mat)
        m = len(mat[0])

        for i in range(n):
            for j in range(m):
                val = mat[i][j]
                coord[val] = (i, j)
                row[i] += 1
                col[j] += 1

        for idx, v in enumerate(arr):
            i, j = coord[v]
            row[i] -= 1
            col[j] -= 1

            if row[i] == 0 or col[j] == 0:
                return idx

        # should never happen
        return -1
        