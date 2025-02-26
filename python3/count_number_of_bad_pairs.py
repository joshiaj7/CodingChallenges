from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(1, n+1):
            ans += i

        h = {}
        for i, v in enumerate(nums):
            total = v - i
            if total not in h:
                h[total] = 1
            else:
                h[total] += 1

        for _, v in h.items():
            for i in range(1, v+1):
                ans -= i

        return ans
        