"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def fib(self, N: int) -> int:
        dp = [0] * (N+1)
        dp[0] = 0

        if N == 0:
            return dp[-1]

        dp[1] = 1

        if N == 1:
            return dp[-1]

        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]
