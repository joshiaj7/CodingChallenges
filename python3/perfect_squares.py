"""
Space   : O(n)
Time    : O(n**2)
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [None] * n

        for i in range(1, n + 1):
            j = 1
            min_val = 10000000

            while j * j <= i:
                min_val = min(min_val, dp[i - j * j])
                j += 1

            dp[i] = min_val + 1

        return dp[-1]
