from collections import defaultdict
from typing import List

"""
Space   : O(n)
Time    : O(nm)
"""

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n  = len(mat), len(mat[0])
        ans = 0

        ones = []
        rowMap = defaultdict(int)
        colMap = defaultdict(int)

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    ones.append((i, j))
                    rowMap[i] += 1
                    colMap[j] += 1

        for i, j in ones:
            if rowMap[i] == 1 and colMap[j] == 1:
                ans += 1

        return ans
