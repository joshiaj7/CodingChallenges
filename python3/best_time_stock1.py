"""
Space   : O(1)
Time    : O(n)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, dp = 10**10, 0
        
        for i in prices:
            print(start)
            start = min(start, i)
            dp = max(dp, i-start)

        return dp
        