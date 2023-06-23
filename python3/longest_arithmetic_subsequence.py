from typing import List

"""
Space   : O(n^2)
Time    : O(n^2)
"""


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = dict()
        for i in range(n):
            for j in range(i+1, n):
                dp[(j, nums[j] - nums[i])] = dp.get((i, nums[j] - nums[i]), 1) + 1
    
        return max(dp.values())
