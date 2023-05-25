"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1

        dp = [1.0] + [0.0] * n
        pts_sum = 1.0

        for i in range(1, n+1):
            dp[i] = pts_sum / maxPts
            if i < k:
                pts_sum += dp[i]
            if i - maxPts >= 0:
                pts_sum -= dp[i - maxPts]

        return sum(dp[k:])
