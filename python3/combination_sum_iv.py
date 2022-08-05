"""
Space   : O(t)
Time    : O(n * t)

Similar to coin change
DP approach
"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums, dp = sorted(nums), [1] + [0] * (target)

        for i in range(target + 1):
            for n in nums:
                if n > i:
                    break
                if n == i:
                    dp[i] += 1
                if n < i:
                    dp[i] += dp[i - n]

        return dp[target]
