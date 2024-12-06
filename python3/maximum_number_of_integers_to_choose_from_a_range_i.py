from typing import List
from collections import defaultdict

"""
Space   : O(m)
Time    : O(n)
"""

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans = 0
        curSum = 0

        d = defaultdict(int)
        for x in banned:
            d[x] = 1
        m = len(banned)

        for i in range(1, n+1):
            if i in d:
                continue

            if curSum + i > maxSum:
                break

            curSum += i
            ans += 1        

        return ans
