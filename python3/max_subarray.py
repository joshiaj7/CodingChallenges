"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -10**10
        dp = 0
        
        for i in nums:
            dp += i
            res = max(dp, res)
            dp = max(dp, 0)

        return res