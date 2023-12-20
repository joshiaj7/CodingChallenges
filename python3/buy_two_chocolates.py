from typing import List

"""
Space   : O(1)
Time    : O(n log n)
"""


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        n = len(prices)
        prices.sort()

        p = prices[0] + prices[1]
        if money - p >= 0:
            return money - p
        
        return money

        