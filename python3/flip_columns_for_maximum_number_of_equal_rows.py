from typing import List
from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0])
        flip = defaultdict(list)

        for i in range(m):
            zero_idxs = []
            one_idxs = []
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_idxs.append(str(j))
                else:
                    one_idxs.append(str(j))

            if zero_idxs:
                s = "-".join(zero_idxs)
                flip[s].append(i)
            else:
                flip["noflip"].append(i)

            if one_idxs:
                s = "-".join(one_idxs)
                flip[s].append(i)
            else:
                flip["noflip"].append(i)

        for v in flip.values():
            ans = max(ans, len(v))

        return ans
