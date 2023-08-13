from typing import List

"""
Space   : O(1)
Time    : O(n)

Rolling DP
"""

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False, False, False, True]

        for i in range(n):
            dp[i % 4] = False

            # first condition
            if i - 1 >= 0 and nums[i] == nums[i-1]:
                dp[i % 4] |= dp[(i - 2) % 4]  

            # second condition
            if i - 2 >= 0 and nums[i] == nums[i-1] == nums[i-2]:
                dp[i % 4] |= dp[(i - 3) % 4]  

            # third condition
            if i - 2 >= 0 and nums[i] == (nums[i-1] + 1) == (nums[i-2] + 2):
                dp[i % 4] |= dp[(i - 3) % 4]  
                
        return dp[(n - 1) % 4]
