"""
Space   : O(amount + 1)
Time    : O((amount + 1) * coins)
DP approach
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [inf] * amount
        n = amount + 1
        coins.sort()

        for c in coins:
            for i in range(n):
                if i - c >= 0:
                    dp[i] = min(dp[i-c] + 1, dp[i])

        return dp[-1] if dp[-1] != inf else -1
