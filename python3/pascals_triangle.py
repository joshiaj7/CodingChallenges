from typing import List

"""
Space   : O(n^2)
Time    : O(n^2)
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(1, numRows+1):
            row = []
            for j in range(i):
                if j == 0 or j == i-1:
                    row.append(1)
                else:
                    row.append(ans[-1][j-1] + ans[-1][j])
            ans.append(row)

        return ans
