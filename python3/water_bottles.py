"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        full, empty = numBottles, 0

        while full > 0:
            ans += full
            empty += full
            full = 0

            full = empty // numExchange
            empty = empty % numExchange 

        return ans
        