"""
Space   : O(1)
Time    : O(n log h)
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        highest = max(piles)
        if n == h:
            return highest

        left, right = 0, highest
        while left < right:
            mid = (left + right) // 2
            
            if mid == 0:
                return 1

            count = 0
            for p in piles:
                count += p // mid
                if p % mid > 0:
                    count += 1 

            if count > h:
                left = mid + 1
            else:
                right = mid
        
        return left
