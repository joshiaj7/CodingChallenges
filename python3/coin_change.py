"""
Space   : O(amount + 1)
Time    : O((amount + 1) * coins)

Method:
DP approach
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        coins.sort()

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i-c] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
