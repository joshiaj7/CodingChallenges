from typing import List
from collections import defaultdict
from bisect import bisect_right

"""
Space   : O(n)
Time    : O(n^2 log n)
"""

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = { -1: 0 }
        arr2.sort()
        for i in arr1:
            tmp = defaultdict(lambda: float('inf'))
            for key in dp:
                if i > key:
                    tmp[i] = min(tmp[i], dp[key])
                loc = bisect_right(arr2, key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]], dp[key]+1)
            dp = tmp

        if dp:
            return min(dp.values())
        return -1
