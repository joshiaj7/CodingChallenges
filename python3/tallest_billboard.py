from typing import List
import collections

"""
Space   : O(nm)
Time    : O(nm)

n = len(rods)
s = sum(rods)
m = all possible sums = min(3^n, s)
"""

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 0
        for x in rods:
            temp = dp.copy()
            for d, y in dp.items():
                temp[d + x] = max(temp[d + x], y)
                temp[abs(d - x)] = max(temp[abs(d - x)], y + min(d, x))
            dp = temp
        return dp[0]
