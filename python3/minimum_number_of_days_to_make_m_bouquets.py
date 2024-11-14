from typing import List

"""
Space   : O(1)
Time    : O(n log n)
Binary search
"""

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if m * k > n:
            return -1

        ans = n

        minDay = min(bloomDay)
        maxDay = max(bloomDay)

        while minDay <= maxDay:
            mid = (minDay + maxDay) // 2

            count = 0
            bouquet = 0
            for i in range(n):
                if bloomDay[i] <= mid:
                    count += 1
                else:
                    count = 0
                
                if count == k:
                    bouquet += 1
                    count = 0

            if bouquet >= m:
                ans = mid
                maxDay = mid - 1
            else:
                minDay = mid + 1


        return ans
        