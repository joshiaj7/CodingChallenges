from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        pref = [0 for _ in range(n+1)]

        for l, r in queries:
            pref[l] += 1
            pref[r+1] -= 1

        curr = 0
        for i in range(n):
            curr += pref[i]
            nums[i] = max(nums[i] - curr, 0)

        return sum(nums) == 0
