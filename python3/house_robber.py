"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        leng = len(nums)
        dp = [0] * leng
        
        for idx in range(leng):
            if idx < 2:
                dp[idx] = nums[idx]
            elif idx == 2:
                dp[idx] = dp[idx-2] + nums[idx]
            else:
                dp[idx]  = max(dp[idx-2], dp[idx-3]) + nums[idx]
            ans = max(dp[idx], ans)
            
        return ans