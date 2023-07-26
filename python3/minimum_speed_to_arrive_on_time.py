from typing import List
from math import ceil

"""
Space   : O(1)
Time    : O(right)
"""

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)

        if sum(dist) <= hour:
            return 1

        left, right = 0, 10 ** 7 + 1
        while left < right:
            mid = (left + right) // 2
            if mid == 0:
                return -1

            arrive_time = 0
            for i, d in enumerate(dist):
                if i == n-1:
                    arrive_time += d / mid
                else:
                    arrive_time += ceil(d / mid)

            if arrive_time > hour:
                left = mid + 1
            else:
                right = mid

        return -1 if left == 10 ** 7 + 1 else left
