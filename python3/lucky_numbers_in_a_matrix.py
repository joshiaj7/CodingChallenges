from typing import List

"""
Space   : O(n)
Time    : O(mn)
"""

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])

        rows, cols = {}, {}
        for i in range(m):
            for j in range(n):
                v =  matrix[i][j]
                if i not in rows:
                    rows[i] = v
                else:
                    rows[i] = min(rows[i], v)

                if j not in cols:
                    cols[j] = v
                else:
                    cols[j] = max(cols[j], v)

        for i in range(len(rows)):
            for j in range(len(cols)):
                if rows[i] == cols[j]:
                    ans.append(rows[i])

        return ans
