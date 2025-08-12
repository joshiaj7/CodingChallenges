"""
Space   : O(n)
Time    : O(nx)
"""

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10 ** 9 + 7

        nums = []
        i = 1
        while i ** x <= n:
            nums.append(i ** x)
            i += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for num in nums:
            for s in range(n, num - 1, -1):
                dp[s] = (dp[s] + dp[s - num]) % mod

        return dp[n]
        