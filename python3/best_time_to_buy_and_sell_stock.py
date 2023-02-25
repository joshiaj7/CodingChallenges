"""
Space   : O(1)
Time    : O(n)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mi = 10000

        for p in prices:
            mi = min(mi, p)
            ans = max(ans, p - mi)

        return ans

        