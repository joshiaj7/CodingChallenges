import math
from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        n = len(dimensions)

        maxDiag = 0
        currDiag = 0
        currArea = 0
        for i in range(n):
            a = dimensions[i][0]
            b = dimensions[i][1]
            currArea = a * b
            currDiag = math.sqrt(a * a + b * b)
            if maxDiag < currDiag:
                maxDiag = currDiag
                ans = currArea
            elif maxDiag == currDiag:
                ans = max(ans, currArea)

        return ans

        