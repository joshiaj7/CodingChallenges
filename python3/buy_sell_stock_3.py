"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstBuy, secondBuy = (10**10) * -1, (10**10) * -1
        firstSold, secondSold = 0, 0
        
        for i in range(len(prices)):
            firstBuy = max(firstBuy, -prices[i])
            firstSold = max(firstSold, firstBuy + prices[i])
            secondBuy = max(secondBuy, firstSold - prices[i])
            secondSold = max(secondSold, secondBuy + prices[i])
        
        return secondSold