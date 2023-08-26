from typing import List

"""
Space   : O(1)
Time    : O(n log n)
"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        ans = 0 
        cur = float('-inf')
        pairs.sort(key=lambda x: x[1])

        for x, y in pairs:
            if cur < x:
                cur = y
                ans += 1

        return ans

