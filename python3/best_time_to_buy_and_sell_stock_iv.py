"""
Space   : O(n)
Time    : O(nk)
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        ans = 0
        if k >= n // 2:
            for i in range(1, n):
                ans += max(prices[i] - prices[i-1], 0)
            return ans

        profits = [0] * n
        for j in range(k):
            preprofit = 0
            for i in range(1, len(prices)):
                profit = prices[i] - prices[i-1]
                preprofit = max(preprofit + profit, profits[i])
                profits[i] = max(profits[i-1], preprofit)

        return profits[-1]
