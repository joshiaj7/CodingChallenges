"""
Space   : O(m)
Time    : O(m.n)
where n = len(nums), m = n / 2
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 == 1:
            return False

        target = s // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for i in nums:
            for j in range(target, i-1, -1):
                dp[j] = dp[j] or dp[j-i]
        return dp[target]
