"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buy, sell = -prices[0], 0
        prev_buy, prev_sell = 0, 0
        for p in prices:
            prev_buy = buy
            buy = max(prev_sell - p, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + p, prev_sell)

        return sell
